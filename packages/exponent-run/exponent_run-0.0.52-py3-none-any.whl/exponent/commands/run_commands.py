import asyncio
import sys
import time
from typing import Optional

import click

from exponent.commands.common import (
    check_inside_git_repo,
    check_running_from_home_directory,
    check_ssl,
    create_chat,
    inside_ssh_session,
    redirect_to_login,
    start_client,
)
from exponent.commands.settings import use_settings
from exponent.commands.types import exponent_cli_group
from exponent.commands.utils import (
    ConnectionTracker,
    Spinner,
    launch_exponent_browser,
    print_exponent_message,
)
from exponent.core.config import Settings

try:
    # this is an optional dependency for python <3.11
    from async_timeout import timeout
except ImportError:  # pragma: no cover
    from asyncio import timeout  # type: ignore


@exponent_cli_group()
def run_cli() -> None:
    """Run AI-powered chat sessions."""
    pass


@run_cli.command()
@click.option(
    "--chat-id",
    help="ID of an existing chat session to reconnect",
    required=False,
)
@click.option(
    "--prompt",
    help="Start a chat with a given prompt.",
)
@click.option(
    "--benchmark",
    is_flag=True,
    help="Enable benchmarking mode",
)
@use_settings
def run(
    settings: Settings,
    chat_id: Optional[str] = None,
    prompt: Optional[str] = None,
    benchmark: bool = False,
) -> None:
    """Start or reconnect to an Exponent session."""
    if not settings.api_key:
        redirect_to_login(settings)
        return

    check_running_from_home_directory()
    check_inside_git_repo(settings)
    check_ssl()

    start_ts = time.time()
    api_key = settings.api_key
    base_url = settings.base_url
    base_api_url = settings.base_api_url
    loop = asyncio.get_event_loop()
    chat_uuid = chat_id or loop.run_until_complete(create_chat(api_key, base_api_url))

    if chat_uuid is None:
        sys.exit(1)

    if (
        (not benchmark)
        and (not prompt)
        and (not inside_ssh_session())
        # If the user specified a chat ID, they probably don't want to re-launch the chat
        and (not chat_id)
    ):
        # Open the chat in the browser
        launch_exponent_browser(settings.environment, base_url, chat_uuid)

    print_exponent_message(base_url, chat_uuid)
    print()

    connection_tracker = ConnectionTracker()

    client_fut = loop.create_task(
        start_client(
            api_key,
            base_api_url,
            chat_uuid,
            prompt,
            benchmark,
            connection_tracker,
        )
    )

    conn_fut = loop.create_task(handle_connection_changes(connection_tracker, start_ts))

    _, pending = loop.run_until_complete(
        asyncio.wait({client_fut, conn_fut}, return_when=asyncio.FIRST_COMPLETED)
    )

    print("Disconnected upon user request, shutting down...")

    for task in pending:
        task.cancel()


async def handle_connection_changes(
    connection_tracker: ConnectionTracker, start_ts: float
) -> None:
    try:
        async with timeout(5):
            assert await connection_tracker.next_change()
            print(ready_message(start_ts))
    except TimeoutError:
        spinner = Spinner("Connecting...")
        spinner.show()
        assert await connection_tracker.next_change()
        spinner.hide()
        print(ready_message(start_ts))

    while True:
        assert not await connection_tracker.next_change()

        print("Disconnected...", end="")
        await asyncio.sleep(1)
        spinner = Spinner("Reconnecting...")
        spinner.show()
        assert await connection_tracker.next_change()
        spinner.hide()
        print("\x1b[1;32m✓ Reconnected", end="")
        sys.stdout.flush()
        await asyncio.sleep(1)
        print("\r\x1b[0m\x1b[2K", end="")
        sys.stdout.flush()


def ready_message(start_ts: float) -> str:
    elapsed = round(time.time() - start_ts, 2)
    return f"\x1b[32m✓\x1b[0m Ready in {elapsed}s"
