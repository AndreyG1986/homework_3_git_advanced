import re

import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


# честно говоря я не знаю как это работает (5-10 строки), но другого решения я не нашел
# особенно то что в скобках в 5ой строке непонятно
@pytest.mark.parametrize("numbers", ["123456789012345", "12345678901234"])
def test_get_mask_card_number_check_qty_symbols(numbers):
    with pytest.raises(ValueError) as exc_info:
        if len(numbers) != 16:
            raise ValueError("Некорректное число символов. Должно быть 16 цифр без пробелов и букв")
    assert str(exc_info.value) == "Некорректное число символов. Должно быть 16 цифр без пробелов и букв"


@pytest.mark.parametrize(
    "number, expected_exception",
    [
        ("700079489604635 ", ValueError),
        ("700079489604635F", ValueError),
        ("7000792289606361", "7000 79** **** 6361"),
    ],
)
def test_get_mask_card_number(number, expected_exception):
    if expected_exception == ValueError:
        with pytest.raises(ValueError, match="Некорректный тип символов. Должно быть 16 цифр без пробелов и букв"):
            get_mask_card_number(number)
    else:
        assert get_mask_card_number(number) == "7000 79** **** 6361"


@pytest.mark.parametrize("numbers", ["123456789012345", "12345678901234"])
def test_get_mask_account_check_qty_symbols(numbers):
    with pytest.raises(ValueError) as exc_info:
        if len(numbers) != 20:
            raise ValueError("Некорректное число символов. Должно быть 20 цифр без пробелов и букв")
    assert str(exc_info.value) == "Некорректное число символов. Должно быть 20 цифр без пробелов и букв"


@pytest.mark.parametrize(
    "number, expected_exception",
    [
        ("7365410843013587430 ", ValueError),
        ("7365410843013587430G", ValueError),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(number, expected_exception):
    if expected_exception == ValueError:
        with pytest.raises(ValueError, match="Некорректный тип символов. Должно быть 20 цифр без пробелов и букв"):
            get_mask_account(number)
    else:
        assert get_mask_account(number) == "**4305"


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        # Тесты для номеров карт
        ("Visa Platinum 7000792289606361", "7000792289606361"),
        ("MasterCard 1234567812345678", "1234567812345678"),
        ("МИР 1234123412341234", "1234123412341234"),
        ("Card 1234567890123456", "1234567890123456"),
        # Тесты для номеров счетов
        ("Счет 64686473678894779589", "64686473678894779589"),
        ("Счет 12345678901234567890", "12345678901234567890"),
        ("Счет 12345678901234567890", "12345678901234567890"),
        # Граничные случаи и некорректные данные
        ("", ""),
    ],
)
def test_mask_account_card(input_data, expected_output):
    """Параметризованный тест для функции mask_account_card"""
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize("date_info, expected_date", [("2025-02-11T02:26:18.671407", "11.02.2025")])
def test_check_date_reformat(date_info, expected_date):
    assert get_date(date_info) == expected_date


@pytest.mark.parametrize("date_info, expected_exception", [("43563456346", ValueError)])
def test_date_format_validity(date_info, expected_exception):
    if not re.match(r"^\d{4}-\d{2}-\d{2}T", date_info) and expected_exception:
        with pytest.raises(ValueError, match="Неверный формат даты"):
            get_date(date_info)


def test_sort_by_state(unsorted_list_of_transactions, executed_list):
    assert filter_by_state(unsorted_list_of_transactions) == executed_list


def test_sort_by_date(unsorted_list_of_transactions, sorted_by_day_list):
    assert sorted_by_day_list, sort_by_date(unsorted_list_of_transactions) == sorted_by_day_list
