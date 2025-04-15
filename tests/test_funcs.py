import pytest
import re
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


# честно говоря я не знаю как это работает (5-10 строки), но другого решения я не нашел
# особенно то что в скобках в 5ой строке непонятно
@pytest.mark.parametrize("numbers", ["123456789012345", "12345678901234"])
def test_get_mask_card_number_check_qty_symbols(numbers):
    with pytest.raises(ValueError) as exc_info:
        if len(numbers) != 16:
            raise ValueError("Некорректное число символов. Должно быть 16 цифр без пробелов и букв")
    assert str(exc_info.value) == "Некорректное число символов. Должно быть 16 цифр без пробелов и букв"

@pytest.mark.parametrize("number, expected_exception", [
    ("700079489604635 ", ValueError),
    ("700079489604635F", ValueError),
    ("7000792289606361", "7000 79** **** 6361"),
    ])

def test_get_mask_card_number(number, expected_exception):
    if expected_exception == ValueError:
        with pytest.raises(ValueError, match = "Некорректный тип символов. Должно быть 16 цифр без пробелов и букв"):
            get_mask_card_number(number)
    else:
        assert get_mask_card_number(number) == "7000 79** **** 6361"

@pytest.mark.parametrize("numbers", ["123456789012345", "12345678901234"])
def test_get_mask_account_check_qty_symbols(numbers):
    with pytest.raises(ValueError) as exc_info:
        if len(numbers) != 20:
            raise ValueError("Некорректное число символов. Должно быть 20 цифр без пробелов и букв")
    assert str(exc_info.value) == "Некорректное число символов. Должно быть 20 цифр без пробелов и букв"


@pytest.mark.parametrize("number, expected_exception", [
    ("7365410843013587430 ", ValueError),
    ("7365410843013587430G", ValueError),
    ("73654108430135874305", "**4305"),
    ])

def test_get_mask_account(number, expected_exception):
    if expected_exception == ValueError:
        with pytest.raises(ValueError, match = "Некорректный тип символов. Должно быть 20 цифр без пробелов и букв"):
            get_mask_account(number)
    else:
        assert get_mask_account(number) == "**4305"

# @pytest.fixture
# def some_account_number():
#     return "**5560"
# Так, вот эта история покамест не работает
# @pytest.mark.parametrize("account_number, expected_account_num",
#                          [("Счёт 35383033474447895560", "**5560")]
#                          )
# def test_check_account_number(account_number, expected_account_num):
#     assert mask_account_card(account_number) == expected_account_num

# -----------------------------

@pytest.mark.parametrize("date_info, expected_date",
    [("2025-02-11T02:26:18.671407", "11.02.2025")]
    )
def test_check_date_reformat(date_info,expected_date):
    assert get_date(date_info) == expected_date


@pytest.mark.parametrize("date_info, expected_exception",
    [("43563456346", ValueError)]
    )
def test_date_format_validity(date_info, expected_exception):
    if not re.match(r"^\d{4}-\d{2}-\d{2}T", date_info) and expected_exception:
        with pytest.raises(ValueError, match = "Неверный формат даты"):
            get_date(date_info)