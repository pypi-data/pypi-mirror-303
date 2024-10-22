from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Optional, TypeVar, Union

from exponent.core.types.event_types import (
    CodeBlockEvent,
    CommandEvent,
    FileWriteEvent,
    LocalEventType,
)
import websockets.client
import websockets.exceptions
from httpx import (
    AsyncClient,
    codes as http_status,
)
from pydantic import BaseModel

from exponent.commands.utils import ConnectionTracker
from exponent.core.remote_execution import files, system_context
from exponent.core.remote_execution.code_execution import execute_code
from exponent.core.remote_execution.command_execution import execute_command
from exponent.core.remote_execution.file_write import execute_file_write
from exponent.core.remote_execution.session import (
    RemoteExecutionClientSession,
    get_session,
)
from exponent.core.remote_execution.types import (
    CLIConnectedState,
    CodeExecutionRequest,
    CommandRequest,
    CreateChatResponse,
    ExecutionEndResponse,
    FileWriteRequest,
    GetAllTrackedFilesRequest,
    GetFileAttachmentRequest,
    GetFileAttachmentsRequest,
    GetMatchingFilesRequest,
    HeartbeatInfo,
    ListFilesRequest,
    RemoteExecutionRequestType,
    RemoteExecutionResponseType,
    StartChatRequest,
    StartChatResponse,
    SystemContextRequest,
    UseToolsConfig,
)
from exponent.core.remote_execution.utils import (
    assert_unreachable,
    convert_event_to_execution_request,
    deserialize_api_response,
    deserialize_request_data,
    serialize_message,
)

logger = logging.getLogger(__name__)


TModel = TypeVar("TModel", bound=BaseModel)


class RemoteExecutionClient:
    def __init__(
        self,
        session: RemoteExecutionClientSession,
    ):
        self.current_session = session

        self.file_cache: files.FileCache = files.FileCache(session.working_directory)

    @property
    def working_directory(self) -> str:
        return self.current_session.working_directory

    @property
    def api_client(self) -> AsyncClient:
        return self.current_session.api_client

    async def run_connection(  # noqa: PLR0915,PLR0912
        self,
        chat_uuid: str,
        connection_tracker: Optional[ConnectionTracker] = None,
    ) -> None:
        stop = False

        self.current_session.set_chat_uuid(chat_uuid)

        async for websocket in self.ws_connect(
            f"/api/ws/chat/{chat_uuid}",
        ):
            if connection_tracker is not None:
                await connection_tracker.set_connected(True)

            beats: asyncio.Queue[HeartbeatInfo] = asyncio.Queue()
            requests: asyncio.Queue[RemoteExecutionRequestType] = asyncio.Queue()
            results: asyncio.Queue[RemoteExecutionResponseType] = asyncio.Queue()

            async def beat() -> None:
                while True:
                    info = self.get_heartbeat_info()
                    await beats.put(info)
                    await asyncio.sleep(3)

            # Lock to ensure that only one executor can grab a
            # request at a time.
            requests_lock = asyncio.Lock()

            # Lock to ensure that only one executor can put a
            # result in the results queue at a time.
            results_lock = asyncio.Lock()

            async def executor() -> None:
                # We use locks here to protect the request/result
                # queues from being accessed by multiple executors.
                while True:
                    async with requests_lock:
                        request = await requests.get()

                    # Note that we don't want to hold the lock here
                    # because we want other executors to be able to
                    # grab requests while we're handling a request.
                    response = await self.handle_request(request)

                    async with results_lock:
                        await results.put(response)

            beat_task = asyncio.create_task(beat())

            # Two parallel executors to handle requests
            executor_tasks = [
                asyncio.create_task(executor()),
                asyncio.create_task(executor()),
            ]

            try:
                while True:
                    recv = asyncio.create_task(websocket.recv())
                    get_beat = asyncio.create_task(beats.get())
                    get_result = asyncio.create_task(results.get())

                    done, pending = await asyncio.wait(
                        [recv, get_beat, get_result],
                        return_when=asyncio.FIRST_COMPLETED,
                    )

                    for task in pending:
                        task.cancel()

                        try:
                            await task
                        except asyncio.CancelledError:
                            pass

                    if recv in done:
                        msg = json.loads(str(recv.result()))

                        if msg["type"] == "request":
                            data = json.dumps(msg["data"])
                            request = deserialize_request_data(data)
                            await requests.put(request)

                    elif get_beat in done:
                        info = get_beat.result()
                        data = json.loads(info.model_dump_json())
                        msg = json.dumps({"type": "heartbeat", "data": data})
                        await websocket.send(msg)

                    elif get_result in done:
                        response = get_result.result()
                        data = json.loads(serialize_message(response))
                        msg = json.dumps({"type": "result", "data": data})
                        await websocket.send(msg)

            except websockets.exceptions.ConnectionClosed as e:
                if e.rcvd is not None and e.rcvd.code == 1000:  # noqa: PLR2004
                    stop = True
            except TimeoutError:
                pass

            beat_task.cancel()

            for executor_task in executor_tasks:
                executor_task.cancel()

            if stop:
                break

            if connection_tracker is not None:
                await connection_tracker.set_connected(False)

    async def check_remote_end_event(self, chat_uuid: str) -> bool:
        response = await self.api_client.get(
            f"/api/remote_execution/{chat_uuid}/execution_end",
        )
        execution_end_response = await deserialize_api_response(
            response, ExecutionEndResponse
        )
        return execution_end_response.execution_ended

    async def create_chat(self) -> CreateChatResponse:
        response = await self.api_client.post(
            "/api/remote_execution/create_chat",
        )
        return await deserialize_api_response(response, CreateChatResponse)

    async def start_chat(
        self, chat_uuid: str, prompt: str, use_tools_config: UseToolsConfig
    ) -> StartChatResponse:
        response = await self.api_client.post(
            "/api/remote_execution/start_chat",
            json=StartChatRequest(
                chat_uuid=chat_uuid,
                prompt=prompt,
                use_tools_config=use_tools_config,
            ).model_dump(),
            timeout=60,
        )
        return await deserialize_api_response(response, StartChatResponse)

    def get_heartbeat_info(self) -> HeartbeatInfo:
        return HeartbeatInfo(
            system_info=system_context.get_system_info(self.working_directory),
        )

    async def send_heartbeat(self, chat_uuid: str) -> CLIConnectedState:
        logger.info(f"Sending heartbeat for chat_uuid {chat_uuid}")
        heartbeat_info = self.get_heartbeat_info()
        response = await self.api_client.post(
            f"/api/remote_execution/{chat_uuid}/heartbeat",
            content=heartbeat_info.model_dump_json(),
            timeout=60,
        )
        if response.status_code != http_status.OK:
            raise Exception(
                f"Heartbeat failed with status code {response.status_code} and response {response.text}"
            )
        connected_state = await deserialize_api_response(response, CLIConnectedState)
        logger.info(f"Heartbeat response: {connected_state}")
        return connected_state

    async def handle_request(
        self, request: Union[RemoteExecutionRequestType, LocalEventType]
    ) -> RemoteExecutionResponseType:
        if isinstance(request, (CodeBlockEvent, FileWriteEvent, CommandEvent)):
            request = convert_event_to_execution_request(request)

        response: RemoteExecutionResponseType
        if isinstance(request, CodeExecutionRequest):
            response = await execute_code(
                request,
                self.current_session,
                working_directory=self.working_directory,
            )
        elif isinstance(request, FileWriteRequest):
            response = execute_file_write(
                request,
                working_directory=self.working_directory,
            )
        elif isinstance(request, ListFilesRequest):
            response = await files.list_files(request)
        elif isinstance(request, GetFileAttachmentRequest):
            response = await files.get_file_attachment(request, self.working_directory)
        elif isinstance(request, GetFileAttachmentsRequest):
            response = await files.get_file_attachments(request, self.working_directory)
        elif isinstance(request, GetMatchingFilesRequest):
            response = await files.get_matching_files(request, self.file_cache)
        elif isinstance(request, SystemContextRequest):
            response = system_context.get_system_context(
                request, self.working_directory
            )
        elif isinstance(request, GetAllTrackedFilesRequest):
            response = await files.get_all_tracked_files(
                request, self.working_directory
            )
        elif isinstance(request, CommandRequest):
            response = await execute_command(request, self.working_directory)
        else:
            assert_unreachable(request)
        return response

    def ws_connect(self, path: str) -> websockets.client.connect:
        base_url = (
            str(self.api_client.base_url)
            .replace("http://", "ws://")
            .replace("https://", "wss://")
        )

        url = f"{base_url}{path}"
        headers = {"api-key": self.api_client.headers["api-key"]}

        return websockets.client.connect(
            url, extra_headers=headers, timeout=10, ping_timeout=10
        )

    @staticmethod
    @asynccontextmanager
    async def session(
        api_key: str, base_url: str, working_directory: str
    ) -> AsyncGenerator[RemoteExecutionClient, None]:
        async with get_session(working_directory, base_url, api_key) as session:
            yield RemoteExecutionClient(session)
