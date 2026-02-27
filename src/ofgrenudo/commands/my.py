import typer

from ofgrenudo.discord import display_discord
from ofgrenudo.website import display_website

cli = typer.Typer(help="Get information about me", no_args_is_help=True)


@cli.command(help="Display my discord username")
def discord():
    display_discord()


@cli.command(help="Display my website")
def website():
    display_website()


# maybe fits in a launch command.
# i.e. launch website
# @cli.command(help="Open my website in a browser")
# def launch_my_website():
#     open_website()
