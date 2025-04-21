import re
from typing import Union


def mask_account_card(some_card_number: Union[str]) -> str:
    """Функция mask_account_card принимает на вход номер карты в виде
    cтроки типа: "Visa Platinum 7000792289606361" или "Счет 64686473678894779589"
    и возвращает номер карты, либо номер счёта"""

    card_number = ""
    account_number = ""

    # Условия для карты
    if "Счет" not in some_card_number:
        for symbol in some_card_number:
            if symbol.isdigit():
                card_number += symbol

    # Условие для счета
    if "Счет" in some_card_number:
        for symbol in some_card_number:
            if symbol.isdigit():
                account_number += symbol

        return account_number

    else:

        return card_number


def get_date(some_date: Union[str]) -> str:
    """Функция get_date принимает на вход строку и отдает
    корректный результат в формате 11.07.2018"""
    date = ""
    splitted_date = ""
    year = ""
    month = ""
    day = ""

    if not re.match(r"^\d{4}-\d{2}-\d{2}T", some_date):
        raise ValueError("Неверный формат даты")
    for index in range(0, 10):
        date += some_date[index]

    splitted_date = date.split("-")
    year = splitted_date[0]
    month = splitted_date[1]
    day = splitted_date[2]
    date = f"{day}.{month}.{year}"

    return date
