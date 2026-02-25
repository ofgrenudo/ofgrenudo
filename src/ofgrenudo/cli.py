from __future__ import annotations

import argparse
import importlib.metadata
import sys

DISCORD_HANDLE = "ofgrenudo"
GITHUB_URL = "https://github.com/ofgrenudo"
WEBSITE = "https://unorthodoxdev.net"


def _version() -> str:
    return importlib.metadata.version("ofgrenudo")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="ofgrenudo",
        description="A CLI app that tells you more about me...",
    )
    p.add_argument("--version", action="store_true", help="Show version and exit")

    sub = p.add_subparsers(dest="cmd", required=False)

    sub.add_parser("discord", help="Show Discord contact")
    sub.add_parser("links", help="Show links (GitHub, etc.)")
    sub.add_parser("about", help="Short about blurb")

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.version:
        print(_version())
        return 0

    cmd = args.cmd or "about"

    if cmd == "discord":
        print(f"Discord: {DISCORD_HANDLE}")
        return 0

    if cmd == "links":
        print(f"GitHub: {GITHUB_URL}")
        print(f"Website: {WEBSITE}")
        return 0

    # default: about
    print("Hello World Wide Web")
    print(f"Reach me on Discord: @{DISCORD_HANDLE}")
    print("Links:")
    print(f"  {GITHUB_URL}")
    print("  https://unorthodoxdev.net/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
