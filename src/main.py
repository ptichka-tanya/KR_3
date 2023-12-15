from datetime import datetime

from src.config import TRANSACTIONS_PATH
from src.functions import mask_card_acc_number, format_date, load_data


def get_5_last_transactions(path: str):
    data: list[dict] = load_data(path)

    executed_transactions: list = [transaction for transaction in data if transaction.get("state") == "EXECUTED"]

    last_5_transactions: list = sorted(executed_transactions,
                                       key=lambda x: datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f'),
                                       reverse=True)[:5]

    transactions_output = []

    for transaction in last_5_transactions:
        date = format_date(transaction['date'])
        masked_to = mask_card_acc_number(transaction['to'])
        amount = transaction['operationAmount']['amount']
        currency = transaction['operationAmount']['currency']['name']
        description = transaction['description']
        if 'from' in transaction:
            masked_from = mask_card_acc_number(transaction['from'])
        else:
            masked_from = ''
        transactions_output.append(f"{date} {description}\n{masked_from} -> {masked_to}\n{amount} {currency}\n")

    return transactions_output


def main():
    for transaction in get_5_last_transactions(TRANSACTIONS_PATH):
        print(transaction)


if __name__ == '__main__':
    main() # pragma: no cover
