import os

from ofgrenudo.config import WEBSITE


def display_website():
    print(f"My Website: {WEBSITE}")


def open_website():
    if os.name == "posix":
        os.system("open " + str(WEBSITE))
    elif os.name == "nt":
        os.system("start " + str(WEBSITE))
