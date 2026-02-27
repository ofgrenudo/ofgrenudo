import typer

from ofgrenudo.bashrc import config_bashrc, reset_bashrc, save_bashrc

cli = typer.Typer(
    help="Manipulate your bashrc, customizing it to my liking", no_args_is_help=True
)


@cli.command(help="Backup your bashrc.")
def save(home_directory: str = "/home/jwintersbro"):
    save_bashrc(home_directory)


@cli.command(help="Restores your bashrc from a backup.")
def restore(home_directory: str = "/home/jwintersbro"):
    reset_bashrc(home_directory)


@cli.command(help="Install my bashrc configuration.")
def install(home_directory: str = "/home/jwintersbro"):
    config_bashrc(home_directory)
