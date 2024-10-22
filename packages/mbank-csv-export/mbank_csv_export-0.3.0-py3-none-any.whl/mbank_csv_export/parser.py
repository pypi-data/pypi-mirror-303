import csv
import json
import re
from dataclasses import dataclass
from datetime import date
from io import StringIO

from pydantic import BaseModel


class Operation(BaseModel):
    operation_date: date
    operation_description: str
    account_number: str
    operation_name: str
    transaction_amount: float
    transaction_currency: str


class Account(BaseModel):
    name: str
    number: str


@dataclass
class OperationsParser:
    header_separator: str = (
        "#Data operacji;#Opis operacji;#Rachunek;#Kategoria;#Kwota;\n"
    )
    account_regexp: re.Pattern = r"(?P<account_name>[\w ]+) - (?P<account_number>\d+);"

    def parse(self, csv_content: str) -> list[Operation]:
        header, operations_raw = csv_content.split(self.header_separator)
        accounts = self._parse_header(header)

        # Replace redacted account numbers with complete numbers from header
        # For example: `1111 ... 4444` -> `1111222233334444`
        for account in accounts:
            operations_raw = operations_raw.replace(
                f'"{account.name.strip()} {account.number[:4]} ... {account.number[-4:]}"',
                account.number,
            )

        results = []
        for line in operations_raw.splitlines():
            operation = self._parse_single_operation(line)
            results.append(operation)

        return results

    def _parse_header(self, header: str) -> list[Account]:
        return [
            Account(name=group[0], number=group[1])
            for group in re.findall(self.account_regexp, header)
        ]

    def _parse_single_operation(self, raw_operation: str) -> Operation:
        try:
            (
                operation_date,
                operation_description,
                account_number,
                operation_name,
                transaction_amount_with_currency,
                *_,
            ) = raw_operation.split(";")
        except ValueError:
            raise ValueError("Could not properly unpack operations.")

        operation_description = (
            re.sub(r"\s{2,}", "  ", operation_description)
            .removeprefix('"')
            .removesuffix('  "')
        )
        transaction_amount = transaction_amount_with_currency[:-4].replace(",", ".").replace(" ", "")
        transaction_currency = transaction_amount_with_currency[-3:]

        return Operation(
            operation_date=operation_date,
            operation_description=operation_description,
            account_number=account_number,
            operation_name=operation_name,
            transaction_amount=transaction_amount,
            transaction_currency=transaction_currency,
        )


def to_csv(operations: list[Operation]) -> str:
    if not operations:
        return ""

    fieldnames = list(operations[0].model_dump().keys())

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)

    writer.writeheader()

    for operation in operations:
        writer.writerow(operation.model_dump())

    return output.getvalue()


def to_json(operations: list[Operation]) -> str:
    return json.dumps([op.model_dump() for op in operations])
