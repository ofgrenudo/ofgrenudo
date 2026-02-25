import argparse
import datetime
import importlib.metadata


def main() -> None:
    parser = argparse.ArgumentParser(prog="ofgrenudo")
    parser.add_argument("--version", action="store_true", help="Show version")
    args = parser.parse_args()

    if args.version:
        print(importlib.metadata.version("ofgrenudo"))
        return

    print("Hello World")
    print(f"Today is {datetime.date.today()}")
    print("You can reach me @grenudo on Discord")


if __name__ == "__main__":
    main()
