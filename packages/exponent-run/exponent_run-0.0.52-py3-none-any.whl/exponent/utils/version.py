import subprocess
from importlib.metadata import Distribution, PackageNotFoundError
from json import JSONDecodeError
from typing import Literal, Optional, Union, cast

import click
from httpx import Client, HTTPError
from packaging.version import Version


def get_installed_version() -> Union[str, Literal["unknown"]]:
    """Get the installed version of exponent-run.

    Returns:
        The installed version of exponent-run if it can be determined, otherwise "unknown"
    """
    try:
        return Distribution.from_name("exponent-run").version
    except PackageNotFoundError as e:
        click.echo(f"Error reading version: {e}", err=True)
        return "unknown"


def get_latest_pypi_exponent_version() -> Optional[str]:
    """Get the latest version of Exponent available on PyPI.

    Returns:
        The newest version of Exponent available on PyPI, or None if an error occurred.
    """
    try:
        return cast(
            str,
            (
                Client()
                .get("https://pypi.org/pypi/exponent-run/json")
                .json()["info"]["version"]
            ),
        )
    except (HTTPError, JSONDecodeError, KeyError):
        click.secho(
            "An unexpected error occurred communicating with PyPi, please check your network and try again.",
            fg="red",
        )
        return None


def check_exponent_version() -> Optional[tuple[str, str]]:
    """Check if there is a newer version of Exponent available on PyPI .

    Returns:
        None
    """

    installed_version = get_installed_version()
    if installed_version == "unknown":
        click.secho("Unable to determine current Exponent version.", fg="yellow")
        return None

    if (latest_version := get_latest_pypi_exponent_version()) and Version(
        latest_version
    ) > Version(installed_version):
        return installed_version, latest_version

    return None


def upgrade_exponent(
    *,
    current_version: str,
    new_version: str,
    force: bool,
) -> None:
    """Upgrade Exponent to the passed in version.

    Args:
        current_version: The current version of Exponent.
        new_version: The new version of Exponent.
        force: Whether to force the upgrade without prompting for confirmation.

    Returns:
        None
    """
    upgrade_command = ["pip", "install", "--upgrade", "exponent-run"]

    if not force:
        click.secho(
            f"New version available: exponent-run=={new_version} (current: {current_version})\n"
            f"Update command: '{' '.join(upgrade_command)}'",
            fg="yellow",
            bold=True,
        )

        if not click.confirm("Update now?", default=True):
            click.secho("Aborted.", fg="red")
            return
    else:
        click.echo(f"Current version: {current_version}")
        click.echo(f"New version available: {new_version}")

    click.secho("Updating...", bold=True, fg="yellow")
    subprocess.check_call(upgrade_command)

    click.secho(f"Successfully upgraded Exponent to version {new_version}!", fg="green")
