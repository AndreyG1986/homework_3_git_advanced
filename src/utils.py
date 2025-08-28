import json
import os
from pathlib import Path


PATH_TO_FILE = Path(__file__).parent.parent / "data" / "operations.json"
# PATH_TO_FILE_OPERATIONS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

def get_list_of_transactions(path:str):
    """ Получение списка транзакций из json файла"""
    sum_of_transactions = 0.0
    currency_from = []

    try:
        with path.open("r", encoding="utf-8-sig") as operations_file:
            try:
                operations_data = json.load(operations_file)
            except json.JSONDecodeError:
                print("Запись содержит ошибки")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []

    # transactions_list = operations_data
    # amount_transactions_list = [float(transaction.get('operationAmount', {}).get('amount', 0)) for transaction in operations_data]
    #
    # currency_from= [transaction.get('operationAmount', {}).get('currency', {}).get('code',{}) for transaction in operations_data]

    # sum_of_transactions = sum(transactions_list)
    # for i in amount_transactions_list:
    #     sum_of_transactions += i

    # print(amount_transactions_list)
    # print(type(amount_transactions_list))
    # print()
    # print(sum_of_transactions)
    # print()
    # print(currency_from)
    # print()
    # print(operations_data)
    # print()
    # print(len(operations_data))

    return operations_data

if __name__ == "__main__":
    print(get_list_of_transactions(PATH_TO_FILE))
    # print(PATH_TO_FILE)
    # print(transactions_list)
