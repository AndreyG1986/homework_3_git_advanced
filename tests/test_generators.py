import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_usd_transactions(all_transactions, sorted_by_currency_usd):
    # Фильтруем и сразу преобразуем в список
    filtered = list(filter_by_currency(all_transactions, "USD"))

    # Остальные проверки остаются такими же
    assert len(filtered) == 3
    for transaction in filtered:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"
    assert filtered == sorted_by_currency_usd


def test_transaction_descriptions(all_descriptions, all_transactions):
    # Фильтруем и сразу преобразуем в список
    filtered = list(transaction_descriptions(all_transactions))
    assert filtered == all_descriptions


def test_card_number_generator(generated_numbers, start=4, end=8, template="0000 0000 0000 000"):
    expected_list = []
    for i in range(start, end):
        expected_list.append(template + str(i))

    assert expected_list == generated_numbers
