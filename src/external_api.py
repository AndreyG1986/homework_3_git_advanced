import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

currency_from = "USD"
currency_to = "RUB"
PATH_TO_FILE_OPERATIONS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


"""Функция конвертации валюты"""


def convert_to_rubles(transaction: dict) -> float:
    currency_to = "RUB"
    currency_from = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
    payload = {}
    headers = {"apikey": f"{API_KEY}"}

    if currency_from == "RUB":
        return amount
    elif currency_from == {}:
        return amount
    else:
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text

        if status_code == 200:

            python_response = json.loads(result)
            amount = float(python_response.get("result", 0))
            return amount


print(
    convert_to_rubles(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
    )
)
