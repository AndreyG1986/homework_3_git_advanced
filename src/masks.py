import logging
from pathlib import Path
from typing import Union

# Подготовим папку под логи
LOG_DIR = Path("../logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Настройка логирования: пишем и в файл, и в консоль
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_DIR / "utils.log", mode="w", encoding="utf-8"), logging.StreamHandler()],
)

masks_logger = logging.getLogger("app.masks")


def get_mask_card_number(num: Union[str, int]) -> str:
    """Функция get_mask_card_number принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    num = str(num)
    symbol_counter = 0
    for symbol in num:
        symbol_counter += 1
    if symbol_counter == 16:
        new_string = num[0:4] + " " + num[4:6] + "** " + "**** " + num[12:]
        masks_logger.info("Номер карты успешно скрыт")
    else:
        masks_logger.error("Входные данные для номера карты содержат ошибку")
        raise ValueError("Некорректное число символов. Должно быть 16 цифр без пробелов и букв")

    if any(char.isalpha() or char == " " for char in num):
        masks_logger.error("Входные данные для номера карты содержат ошибку")
        raise ValueError("Некорректный тип символов. Должно быть 16 цифр без пробелов и букв")

    return new_string


def get_mask_account(num: Union[str, int]) -> str:
    """Функция get_mask_account принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX."""
    num = str(num)
    mask_account = ""
    if len(num) == 20:
        mask_account = "**" + num[-4:]
        masks_logger.info("Номер счёта успешно скрыт")
    else:
        masks_logger.error("Входные данные для номера счёта содержат ошибку")
        raise ValueError("Некорректное число символов. Должно быть 20 цифр без пробелов и букв")

    if any(char.isalpha() or char == " " for char in num):
        masks_logger.error("Входные данные для номера счёта содержат ошибку")
        raise ValueError("Некорректный тип символов. Должно быть 20 цифр без пробелов и букв")

    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number("7000794896046356"))
    print(get_mask_account("35383033474447895560"))
