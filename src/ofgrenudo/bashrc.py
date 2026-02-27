import os
import os.path
from pathlib import Path

from rich import print

from ofgrenudo.config import (
    BASHRC,
    BASHRC_BACK,
    COMMANDS_ALIAS,
    LS_ALIAS,
    ZSHRC,
    ZSHRC_BACK,
)

_all_aliases = [LS_ALIAS, COMMANDS_ALIAS]


def _expand(path: str) -> str:
    # Expand environment variables first
    path = os.path.expandvars(path)

    # If it's not using "~", we're done.
    if not path.startswith("~"):
        return str(Path(path))

    # Try normal expanduser
    try:
        return str(Path(path).expanduser())
    except RuntimeError:
        # Fallback: use $HOME if available
        home = os.environ.get("HOME")
        if home:
            if path == "~":
                return home
            if path.startswith("~/"):
                return os.path.join(home, path[2:])
        raise RuntimeError(
            "Could not determine home directory. "
            "Set the HOME environment variable or pass an absolute path."
        )


def _copy_file(source_file: str, destination_file: str):
    import shutil

    if source_file is None or source_file == "":
        raise TypeError("You must provide a source file.")
    if destination_file is None or destination_file == "":
        raise TypeError("You must provide a destination file.")

    source_file = _expand(source_file)
    destination_file = _expand(destination_file)

    try:
        shutil.copy2(source_file, destination_file)
        print(
            f"[green]Successfully[/green] copied '{source_file}' to '{destination_file}'"
        )
    except shutil.SameFileError:
        print("Error: Source and destination represent the same file.")
    except PermissionError:
        print("Error: Permission denied.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def _delete_file(file_name: str):
    from pathlib import Path

    # missing ok means if it doesnt exist, it still evals to true.
    Path(file_name).unlink(missing_ok=True)


def _check_file_exists(file_name: str) -> bool:
    if os.path.exists(file_name):
        return True
    else:
        return False


def _append_to_rc(home_directory: str, source_file: str):
    for alias in _all_aliases:
        file_name = f"{home_directory}{alias['file_name']}"
        content = alias["content"]
        signature = alias["signature"]

        # 1. check if file exists.
        #   - if file exists, check if content is the same.
        #   - if content is not the same, rewrite file.
        #   - if file does not exist, create it.
        # 2. check if .bashrc has signature
        #   - if signature is not found, append signature to .bashrc
        #   - if signature is found, do nothing
        if _check_file_exists(file_name):
            with open(file_name, "r") as f:
                existing_content = f.read()
            if existing_content != content:
                with open(file_name, "w") as f:
                    f.write(content)
                print(f"[green]Successfully[/green] updated '{file_name}'")
        else:
            with open(file_name, "w") as f:
                f.write(content)
            print(f"[green]Successfully[/green] created '{file_name}'")

        if signature not in open(source_file, "r").read():
            with open(source_file, "a") as f:
                f.write(signature)
            print(
                f"[green]Successfully[/green] appended '{file_name}' to '{source_file}'"
            )


def save_bashrc(home_directory: str):
    if home_directory is None:
        raise TypeError("You must provide a home directory.")
    source_file = f"{home_directory}{BASHRC}"
    destination_file = f"{home_directory}{BASHRC_BACK}"
    _copy_file(source_file, destination_file)


def reset_bashrc(home_directory: str):
    if home_directory is None:
        raise TypeError("You must provide a home directory.")
    source_file = f"{home_directory}{BASHRC_BACK}"
    destination_file = f"{home_directory}{BASHRC}"

    _copy_file(  # copy backup to source
        source_file, destination_file
    )

    # cleanup aliases installed
    for alias in _all_aliases:
        print(
            f"[red]:warning: Removing alias {home_directory}{alias['file_name']}[/red]"
        )
        file_name = f"{home_directory}{alias['file_name']}"
        _delete_file(file_name)

    print("\n\n:zombie: Remember to 'source ~/.bashrc'!")


def config_bashrc(home_directory: str):
    if home_directory is None:
        raise TypeError("You must provide a home directory.")
    source_file = f"{home_directory}{BASHRC}"
    destination_file = f"{home_directory}{BASHRC_BACK}"

    print(f"[bold red]:warning: Making a copy of ~{source_file}[/bold red]")
    _copy_file(source_file, destination_file)
    _append_to_rc(home_directory, source_file)

    source_file = f"{home_directory}{ZSHRC}"
    destination_file = f"{home_directory}{ZSHRC_BACK}"

    print(f"[bold red]:warning: Making a copy of ~{source_file}[/bold red]")
    _copy_file(source_file, destination_file)
    _append_to_rc(home_directory, source_file)

    print("\n\n:zombie: Remember to 'source ~/.bashrc'!")
