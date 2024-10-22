# mbank-csv-export

Hey, if you're looking for a tool that automatically exports your mBank transactions, then you've come to the right place!

Many projects successfully attempt to parse the crappy mBank CSV operations, but few reliably automate the extraction process. 
I adopted a modular architecture:

`mbank-export` exports transaction CSV files from mBank as a string.
 - Uses Playwright for automated browser interactions.
 - Saves browser state to maintain session continuity, minimizing the need for repeated mobile authentication.

`mbank-parser` parses the raw transactions and converts them to a desired data format.

## Installation
```shell
pip install mbank-csv-export
```

## Auth
Set `MBANK_USERNAME` and `MBANK_PASSWORD` environment variables or quick start by running `mbank --username username --password password`.

## CLI
```shell
# Export last month operations, parse and format as clean csv:  
mbank-export | mbank-parser

# Export raw operations data from 2024-05-01 to 2024-09-30:  
mbank-export --date-from '2024-05-01' --date-to '2024-09-30' > raw-operations.txt

# Then parse and format those raw operations into json:  
cat raw-operations.txt | mbank-parser --format json

# Or in one line:  
mbank-export --date-from '2024-05-01' --date-to '2024-09-30' | mbank-parser --format json
```

## Python package
```python
from datetime import date

from mbank_csv_export import (
  MBank, 
  OperationsParser, 
  Operation, 
  to_csv, 
  to_json,
)

mbank = MBank(headless=False)
mbank.login(username="1111222233334444", password="***")

csv_content: str = mbank.export_operations_csv(
    date_from=date(2024, 5, 1), 
    date_to=date(2024, 9, 30)
)

operations: list[Operation] = parse_operations(csv_content)
for operation in operations:
  print(operation)

print(to_json(operations))
```







