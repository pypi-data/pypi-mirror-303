import re

_accounts_regexp = re.compile(r"(?P<account_name>[\w ]+) - (?P<account_number>\d+);")


def parse_raw_operations(csv_content: str) -> list[dict]:
    results = []
    header, data = csv_content.split(
        "#Data operacji;#Opis operacji;#Rachunek;#Kategoria;#Kwota;\n"
    )
    data
    for account_name, account_number in _accounts_regexp.findall(header):
        data = data.replace(
            f'"{account_name.strip()} {account_number[:4]} ... {account_number[-4:]}"',
            account_number,
        )

    for line in data.splitlines():
        try:
            (
                operation_date,
                operation_description,
                account_number,
                operation_name,
                transaction_amount,
                *_,
            ) = line.split(";")
        except ValueError:
            print(line.split(";"))
            return

        operation_description = (
            re.sub(r"\s{2,}", "  ", operation_description)
            .removeprefix('"')
            .removesuffix('  "')
        )
        results.append(
            {
                "operation_date": operation_date,
                "operation_description": operation_description,
                "account_number": account_number,
                "operation_name": operation_name,
                "transaction_amount": transaction_amount,
            }
        )
    return results


def operations_to_csv(operations: list[dict]) -> str:
    if len(operations) == 0:
        return ""
    columns = ",".join(operations[0].keys())
    values = "\n".join(",".join(d.values()) for d in operations)
    return f"{columns}\n{values}"
