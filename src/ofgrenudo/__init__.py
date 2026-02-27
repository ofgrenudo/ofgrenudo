import typer

from ofgrenudo.bashrc import config_bashrc, reset_bashrc, save_bashrc
from ofgrenudo.config import DISCORD, WEBSITE
from ofgrenudo.discord import display_discord
from ofgrenudo.network import get_lan_ip, get_wan_ip
from ofgrenudo.website import display_website, open_website

__ALL__ = [DISCORD, WEBSITE, "display_discord", "display_website", "hello", "main"]

cli = typer.Typer()


@cli.command()
def my_discord():
    display_discord()


@cli.command()
def my_website():
    display_website()


@cli.command()
def lanip():
    get_lan_ip()


@cli.command()
def wanip():
    get_wan_ip()


@cli.command()
def bashrc_save(home_directory: str = "/home/jwintersbro"):
    save_bashrc(home_directory)


@cli.command()
def bashrc_restore(home_directory: str = "/home/jwintersbro"):
    reset_bashrc(home_directory)


@cli.command()
def bashrc_install(home_directory: str = "/home/jwintersbro"):
    config_bashrc(home_directory)


@cli.command()
def launch_my_website():
    open_website()


def main() -> None:
    cli()
