from typing import Union


def get_mask_card_number(num: Union[str, int]) -> str:
    """Функция get_mask_card_number принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    num = str(num)
    symbol_counter = 0
    for symbol in num:
        symbol_counter += 1
    if symbol_counter == 16:
        new_string = num[0:4] + " " + num[4:6] + "** " + "**** "+ num[12:]
    else:
        raise ValueError("Некорректное число символов. Должно быть 16 цифр без пробелов и букв")

    if any(char.isalpha() or char==" " for char in num):
        raise ValueError("Некорректный тип символов. Должно быть 16 цифр без пробелов и букв")

    return new_string


def get_mask_account(num: Union[str, int]) -> str:
    """Функция get_mask_account принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX."""
    num = str(num)
    mask_account = ""
    if len(num) == 20:
        mask_account = "**" + num[-4:]
    else:
        raise ValueError("Некорректное число символов. Должно быть 20 цифр без пробелов и букв")

    if any(char.isalpha() or char==" " for char in num):
        raise ValueError("Некорректный тип символов. Должно быть 20 цифр без пробелов и букв")

    return mask_account
