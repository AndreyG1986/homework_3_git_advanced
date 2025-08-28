import requests
import os
from dotenv import load_dotenv
from src.utils import get_list_of_transactions
from functools import wraps

load_dotenv()

API_KEY = os.getenv("API_KEY")

currency_from = "USD"
currency_to = "RUB"
PATH_TO_FILE_OPERATIONS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
# operations_list = get_list_of_transactions(PATH_TO_FILE_OPERATIONS)

#
# url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount=1"
#
# payload = {}
# headers= {
#   "apikey": f"{API_KEY}"
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text

# print(result)
# print()
# print(PATH_TO_FILE_OPERATIONS)
# print()
# print(operations_list)

"""Здесь начинается моя функция"""
def convert_to_rubles(transaction: dict)-> float:
    currency_to = "RUB"
    currency_from = transaction.get('operationAmount', {}).get('currency', {}).get('code',{})
    amount = float(transaction.get('operationAmount', {}).get('amount', 0))
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
    payload = {}
    headers = {
        "apikey": f"{API_KEY}"
    }
    # python_response = {}
    if currency_from == "RUB":
        return amount
    elif currency_from == {}:
        return amount
    else:
        # response = requests.get ( f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}")
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text
        # print(currency_from)
        # print(amount)
        # print(response.status_code)
        if status_code == 200:
            import json
            python_response = json.loads(result)
            amount = float(python_response.get('result', 0))
            return amount

print(convert_to_rubles({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},))

# #Функция суммирования
# def summator(a,b):
#     return a+b
#
# # Здесь я пытаюсь написать декоратор, который получал бы функцию
# # в качестве аргумента, а отдавал бы сумму транзакций с конвертированной валютой
# def dec_sum_of_transactions(func_recieve_transactions):
#     # Объявляем переменные список транзакций и сумма транзакций
#     sum_list = []
#     sum_result = 0.0
#     # Узнаём у пользователя какое кол-во транзакций он желает суммировать
#     max_len_of_transactons = len(func_recieve_transactions)
#     necessary_qty_of_transactions = input(int(f"Введите необходимое кол-во от 1 до {max_len_of_transactons} транзакций, которое нужно суммировать"))
#     сurrency =  [transaction.get('operationAmount', {}).get('currency', {}).get('code',{}) for transaction in func_recieve_transactions]
#     # Пишем какую-то историю, которая будет конвертировать транзакцию и суммировать
#     # и выдавать некий результат
#     def wrapper(func_convert):
#         # Составляем список и суммируем то кол-во, которое запросил пользователь
#         for operation in func_recieve_transactions:
#             for i in range(necessary_qty_of_transactions):
#                 sum_list.append(operation)
#                 x = int(operation[i])
#                 sum_result += x
#
#         return sum_result
#     return wrapper
#
# # С помощью декоратора пытаемся изменить функцию summator,
# # чтобы она сложила все нужные транзакции.
# @dec_sum_of_transactions
# def summator(a,b):
#     result = a + b
#     return result