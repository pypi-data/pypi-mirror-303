from typing import Optional

import click
import typer

import metamart_cli
from metamart_cli.api.callbacks import default_callback
from metamart_cli.utilities.styling import HAS_RICH, print
from metamart_cli.utilities.telemetry import Telemetry


def result_callback(*args, **kwargs):
    """

    Args:
        *args:
        **kwargs:

    Returns:

    Raises:

    """
    ctx = click.get_current_context()
    command_path = ctx.meta["command_path"]
    if command_path and command_path[0] != "telemetry":
        command = f"metamart {' '.join(command_path)}"
        Telemetry.capture(command)


app = typer.Typer(
    rich_markup_mode="rich" if HAS_RICH else None,
    invoke_without_command=True,
    no_args_is_help=True,
    help="Metamart CLI",
    pretty_exceptions_show_locals=False,
    result_callback=result_callback,
)


@app.callback()
def callback(
    ctx: typer.Context,
    telemetry: Optional[bool] = typer.Option(None, show_default=False, help="Enable or disable telemetry"),
):
    """Metamart CLI

    Args:
        ctx (typer.Context):
        telemetry (Optional[bool], optional):  (Default value = typer.Option(None, show_default=False, help="Enable or disable telemetry"))

    Returns:

    Raises:

    """

    if telemetry is not None:
        from metamart_cli.settings.cache import cache

        cache.set("telemetry_consent", telemetry)

    default_callback(ctx)


@app.command("version", help="Returns the current CLI version")
def get_cli_version():
    print(metamart_cli.__version__)
