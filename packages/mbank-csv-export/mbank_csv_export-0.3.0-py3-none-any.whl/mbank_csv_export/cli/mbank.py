import datetime
import sys
from argparse import ArgumentParser
from pathlib import Path

from dateutil.relativedelta import relativedelta

from mbank_csv_export.mbank import MBank
from mbank_csv_export.settings import Settings


def main():
    settings = Settings()
    argparser = ArgumentParser(prog="mbank")
    argparser.add_argument("--headless", action="store_true", default=False)
    argparser.add_argument(
        "--username",
        type=str,
        default=settings.mbank_username,
        help="or set MBANK_USERNAME env variable",
    )
    argparser.add_argument(
        "--password",
        type=str,
        default=settings.mbank_password,
        help="or set MBANK_PASSWORD env variable",
    )
    argparser.add_argument(
        "--log-level",
        type=str,
        default=settings.mbank_log_level,
        choices=["ERROR", "WARN", "INFO", "DEBUG"],
        help="or set MBANK_LOG_LEVEL env variable",
    )
    argparser.add_argument(
        "--date-from",
        type=lambda s: datetime.datetime.strptime(s, "%Y-%m-%d"),
        default=(datetime.datetime.now() - relativedelta(month=1)).strftime("%Y-%m-%d"),
        help="format YYYY-MM-DD, defaults to date 1 month ago.",
    )
    argparser.add_argument(
        "--date-to",
        type=lambda s: datetime.datetime.strptime(s, "%Y-%m-%d"),
        default=datetime.date.today().strftime("%Y-%m-%d"),
        help="format YYYY-MM-DD, defaults to date today.",
    )
    argparser.add_argument(
        "--output", "-o", type=str, default="-", help="output file path"
    )
    argparser.add_argument("--verbose", action="store_true", default=False)
    args = argparser.parse_args()

    if args.username is None:
        print(
            "Missing username. Use --username <username> argument or set MBANK_USERNAME env variable."
        )
        sys.exit(1)

    if args.password is None:
        print(
            "Missing password. Use --password <password> argument or set MBANK_PASSWORD env variable."
        )
        sys.exit(1)

    if args.verbose:
        args.log_level = "DEBUG"

    mbank = MBank(headless=args.headless, log_level=args.log_level)
    mbank.login(args.username, args.password)
    content = mbank.export_operations_csv(args.date_from, args.date_to)
    content = content.strip()

    if args.output == "-":
        print(content)
    else:
        Path(args.output).write_text(content)


if __name__ == "__main__":
    main()