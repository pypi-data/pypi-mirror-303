import typer
import uv_up
from uv_up.cli import app as uv_up_cli
from uv_version.cli import app as uv_version_cli

cli = typer.Typer(help='uvxt')
cli.add_typer(uv_up_cli, name='up')
cli.add_typer(uv_version_cli, name='version')


def version_callback(value: bool):
    if value:
        print(f'Version of uvxt is {uv_up.__version__}')
        raise typer.Exit()


@cli.callback(invoke_without_command=True)
def callback(  # noqa: C901
    ctx: typer.Context,
    #
    version: bool = typer.Option(
        False,
        '--version',
        callback=version_callback,
        help='Print version of uvxt.',
        is_eager=True,
    ),
):
    pass
