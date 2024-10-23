import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="(Lumos) Connectors CLI")
    subparsers = parser.add_subparsers(dest="command")

    scaffold_parser = subparsers.add_parser("scaffold", help="Create a new connector")
    scaffold_parser.add_argument("name", help="Name of the new connector")
    scaffold_parser.add_argument(
        "directory", type=Path, help="Directory to create the connector in"
    )
    scaffold_parser.add_argument("--force-overwrite", "-f", action="store_true")

    args = parser.parse_args()

    if args.command == "scaffold":
        from connector.scaffold.create import scaffold

        scaffold(args)


if __name__ == "__main__":
    main()
