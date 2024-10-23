import typer

import uv_up
from uv_up.manager import UvUpManager

app = typer.Typer(help='uv-up CLI')


uv_up_manager = UvUpManager()


def version_callback(value: bool):
    if value:
        print(f'Version of uv-up is {uv_up.__version__}')
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def callback(  # noqa: C901
    ctx: typer.Context,
    #
    version: bool = typer.Option(
        False,
        '--version',
        callback=version_callback,
        help='Print version of uv-version.',
        is_eager=True,
    ),
    # Setters
    latest: bool = typer.Option(
        False,
        '--latest',
        help='Set a new version in pyproject.toml.',
        metavar='Default',
        rich_help_panel='uv-version Setters Options',
    ),
):
    pass

    if ctx.invoked_subcommand is None:
        pass


@app.command('up')
def up_command():
    pass


def cli():
    app()
