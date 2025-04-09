from typing import Union


def get_mask_card_number(num: Union[str, int]) -> str:
    """Функция get_mask_card_number принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    num = str(num)
    mask_card_number = num[0:4] + " " + num[4:6] + "** " + "**** " + num[12:]

    return mask_card_number


def get_mask_account(num: Union[str, int]) -> str:
    """Функция get_mask_account принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX."""
    num = str(num)
    mask_account = "**" + num[-4:]

    return mask_account
