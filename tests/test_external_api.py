from unittest import mock
import requests
from dotenv import load_dotenv
from src.utils import get_list_of_transactions
import os
from unittest.mock import patch
from src.external_api import convert_to_rubles

load_dotenv()

API_KEY = os.getenv("API_KEY")

operation = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}
#
# """Здесь начинается моя функция"""
# def convert_to_rubles(transaction: dict)-> float:
#     currency_to = "RUB"
#     currency_from = transaction.get('operationAmount', {}).get('currency', {}).get('code',{})
#     amount = float(transaction.get('operationAmount', {}).get('amount', 0))
#     url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
#     payload = {}
#     headers = {
#         "apikey": f"{API_KEY}"
#     }
#     # python_response = {}
#     if currency_from == "RUB":
#         return amount
#     elif currency_from == {}:
#         return amount
#     else:
#         # response = requests.get ( f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}")
#         response = requests.request("GET", url, headers=headers, data=payload)
#         status_code = response.status_code
#         result = response.text
#         if status_code == 200:
#             import json
#             python_response = json.loads(result)
#             amount = float(python_response.get('result', 0))
#             return amount
#
# print(convert_to_rubles({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},))

@patch('requests.request')
def test_convert_to_rubles_info(mock_get):
    transaction = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}
    currency_to = "RUB"
    currency_from = transaction.get('operationAmount', {}).get('currency', {}).get('code',{})
    amount = float(transaction.get('operationAmount', {}).get('amount', 0))
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
    mock_get.return_value = 2575114.472669
    assert test_convert_to_rubles_info(mock_get)==2575114.472669
    mock_get.assert_called_once_with(url)

if __name__ == "__main__":
    print(test_convert_to_rubles_info(operation))