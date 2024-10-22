import json
import sys
from argparse import ArgumentParser
from pathlib import Path

from mbank_csv_export.parser import operations_to_csv, parse_raw_operations


def main():
    argparser = ArgumentParser(prog="mbank-parser")
    argparser.add_argument(
        "--input",
        "-i",
        type=str,
        default="-",
        help="input file path",
    )
    argparser.add_argument(
        "--output",
        "-o",
        type=str,
        default="-",
        help="output file path",
    )
    argparser.add_argument(
        "--format",
        type=str,
        choices=["json", "csv"],
        default="csv",
    )
    args = argparser.parse_args()

    if args.input != "-" and not Path(args.input).exists():
        print("Error: Input path does not exist.")

    if args.input == "-":
        csv_content: str = sys.stdin.read()
    else:
        csv_content: str = Path(args.input).read_text()

    operations: list[dict] = parse_raw_operations(csv_content)

    if args.format == "json":
        operations_formatted: str = json.dumps(operations)
    elif args.format == "csv":
        operations_formatted: str = operations_to_csv(operations)

    if args.output == "-":
        print(operations_formatted)
    else:
        Path(args.output).write_text(operations_formatted)


if __name__ == "__main__":
    main()