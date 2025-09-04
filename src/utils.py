import json
from pathlib import Path

PATH_TO_FILE = Path(__file__).parent.parent / "data" / "operations.json"


def get_list_of_transactions(path: str):
    """Получение списка транзакций из json файла"""
    sum_of_transactions = 0.0
    currency_from = []

    try:
        with path.open("r", encoding="utf-8-sig") as operations_file:
            try:
                operations_data = json.load(operations_file)
            except json.JSONDecodeError:
                print("Запись содержит ошибки")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []

    return operations_data


if __name__ == "__main__":
    print(get_list_of_transactions(PATH_TO_FILE))
