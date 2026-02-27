from importlib.metadata import version as get_version

import typer

from ofgrenudo.commands.bashrc import cli as bashrc_cli
from ofgrenudo.commands.my import cli as my_cli
from ofgrenudo.commands.network import cli as network_cli

cli = typer.Typer(no_args_is_help=True)
__version__ = get_version("ofgrenudo")


def _version_cb(value: bool) -> None:
    if value:
        typer.echo(f"ofgrenudo v{__version__}")
        raise typer.Exit()


@cli.callback()
def version(
    version: bool = typer.Option(
        False,
        "--version",
        help="Display the version and exit",
        callback=_version_cb,
        is_eager=True,
    ),
) -> None:
    pass


cli.add_typer(network_cli, name="network")
cli.add_typer(my_cli, name="my")
cli.add_typer(bashrc_cli, name="bashrc")


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
