import asyncio
import os
import shutil

STDOUT_FD = 1
STDERR_FD = 2
MAX_TIMEOUT = 300


async def execute_shell(code: str, working_directory: str, timeout: int) -> str:
    timeout = min(timeout, MAX_TIMEOUT)

    shell_path = (
        os.environ.get("SHELL")
        or shutil.which("bash")
        or shutil.which("sh")
        or "/bin/sh"
    )

    process = await asyncio.create_subprocess_exec(
        shell_path,
        "-l",
        "-c",
        code,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=working_directory,
    )

    exit_code = None
    output: list[tuple[int, str]] = []
    assert process.stdout
    assert process.stderr

    stdout_capture_task = asyncio.create_task(
        capture(process.stdout, STDOUT_FD, output)
    )

    stderr_capture_task = asyncio.create_task(
        capture(process.stderr, STDERR_FD, output)
    )

    async def capture_until_exit() -> int:
        await asyncio.wait({stdout_capture_task, stderr_capture_task})
        return await process.wait()

    try:
        exit_code = await asyncio.wait_for(capture_until_exit(), timeout)
    except (TimeoutError, asyncio.TimeoutError):  # noqa: UP041
        process.kill()

    formatted_output = "".join([chunk for (_, chunk) in output]).strip() + "\n\n"

    if exit_code is None:
        formatted_output += f"EXIT CODE: not available - Exponent stopped the command after {timeout} seconds"
    else:
        formatted_output += f"EXIT CODE: {exit_code}"

    return formatted_output


async def capture(
    stream: asyncio.StreamReader, fd: int, output: list[tuple[int, str]]
) -> None:
    while True:
        data = await stream.read(4096)

        if not data:
            break

        output.append((fd, data.decode()))
