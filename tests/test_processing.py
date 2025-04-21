from src.processing import filter_by_state, sort_by_date


def test_sort_by_state(unsorted_list_of_transactions, executed_list):
    assert filter_by_state(unsorted_list_of_transactions) == executed_list


def test_sort_by_date(unsorted_list_of_transactions, sorted_by_day_list):
    assert sorted_by_day_list, sort_by_date(unsorted_list_of_transactions) == sorted_by_day_list


def test_sort_by_date_ascending(unsorted_list_of_transactions, sorted_by_day_list):
    assert sort_by_date(unsorted_list_of_transactions, False) == sorted_by_day_list[::-1]
