import re
from src.file_reader import read_xl_file
from  collections import Counter


data_xl = read_xl_file("../data/transactions_excel.xlsx")

def process_bank_search(operations_list:list[dict], keyword:str)->list[dict]:
    """Функция, которая будет принимать список словарей с данными
    о банковских операциях и строку поиска, а возвращать список словарей,
    у которых в описании есть данная строка"""
    chosen_operations = []
    for operation in operations_list:
        description = operation.get('description', '')
        if isinstance(description, str) and re.search(keyword, description, flags=re.IGNORECASE):
            chosen_operations.append(operation)
    return chosen_operations


def process_bank_operations(operations_data: list[dict], categories: list[str]) -> dict[str, int]:
    """функцию, которая будет принимать список словарей с данными о банковских операциях
    и список категорий операций, а возвращать словарь,
    в котором ключи — это названия категорий, а значения —
    это количество операций в каждой категории.
    Категории операций хранятся в поле description."""
    cats = [c.lower() for c in categories]
    categories_count_list = []
    for op in operations_data:
        desc = str(op.get('description', '')).lower()
        categories_count_list += [c for c in cats if c in desc]
    return dict(Counter(categories_count_list))


if __name__ == "__main__":
    print(process_bank_search(data_xl, "перевод"))
    print(process_bank_operations(data_xl, ['Перевод с карты на карту']))
