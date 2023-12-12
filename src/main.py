from datetime import datetime

from config import TRANSACTIONS_PATH
from functions import mask_card_acc_number, format_date, load_data


def main():
    data: list[dict] = load_data(TRANSACTIONS_PATH)

    executed_transactions: list = [transaction for transaction in data if transaction.get("state") == "EXECUTED"]

    last_5_transactions: list = sorted(executed_transactions,
                                       key=lambda x: datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f'),
                                       reverse=True)[:5]

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
        print(f"{date} {description}\n{masked_from} -> {masked_to}\n{amount} {currency}\n")


if __name__ == '__main__':
    main()
