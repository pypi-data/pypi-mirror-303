import typer

from metamart_cli.api.entrypoint import app
from metamart_cli.utilities.telemetry import capture

telemetry_app = typer.Typer(help="Event Logging Functionality", hidden=True)


@telemetry_app.command("log")
def log(event: str):
    """

    Args:
        event (str):

    Returns:

    Raises:

    """
    capture(event)
