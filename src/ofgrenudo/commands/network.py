import typer

from ofgrenudo.network import get_lan_ip, get_wan_ip

cli = typer.Typer(help="Networking commands", no_args_is_help=True)


@cli.command(
    help="Gets the local IP address of the device. Does not require active internet connection."
)
def lanip():
    get_lan_ip()


@cli.command(
    help="Gets the public IP address of the device. Requires active internet connection."
)
def wanip():
    get_wan_ip()
