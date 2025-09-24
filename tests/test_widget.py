import re

import pytest

from src.widget import get_date, mask_account_card


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
