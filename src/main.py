# from src.utils import get_list_of_transactions,PATH_TO_FILE
from src.file_reader import read_xl_file, read_csv_file
from src.processing import filter_by_state, sort_by_date
from src.search_info import process_bank_search
import os
import json

PATH_TO_FILE_JSON = os.path.join(os.path.dirname(__file__), "../data", "operations.json")


# У меня не заработала функция get_list_of_transactions
# PyCharm стал возвращать логи и зависать, поэтому пишу эту функцию
def get_list_of_transactions_json(path):
    """Получение списка транзакций из json файла"""
    try:
        with open(PATH_TO_FILE_JSON, "r", encoding="utf-8-sig") as file:
        # with path.open("r", encoding="utf-8-sig") as f:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except json.JSONDecodeError as e:
        print("Запись содержит ошибки")
        return []


def find_rub_operations(operations_list:list[dict])->list[dict]:
    target_currency = 'RUB'
    rub_operations = [op for op in operations_list if op.get("operationAmount", {}).get("currency", {}).get("code", {}) == target_currency]
    return rub_operations


def use_app():
    """Функция которая отвечает за основную логику проекта и связывает функциональности между собой"""
    doc = None
    result = None
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    user_input_source = str(input("Чтобы получить информацию о транзакциях из JSON-файла нажмите 1"
                                  "\nЧтобы получить информацию о транзакциях из CSV-файла нажмите 2"
                                  "\nЧтобы получить информацию о транзакциях из из XLSX-файла нажмите 3: "))
    user_input_source = int(user_input_source)
    if user_input_source == 1:
        doc = get_list_of_transactions_json(PATH_TO_FILE_JSON)
    elif user_input_source == 2:
        doc = read_csv_file("../data/transactions.csv")
    elif user_input_source == 3:
        doc = read_xl_file("../data/transactions_excel.xlsx")

    user_input_status = str(input("Выберите статус интересующих вас операций executed/cancelled: ")).upper()
    filter_by_state_result = filter_by_state(doc,user_input_status)

    # print(filter_by_state_result)

    user_input_sort_by_date = str(input("Отсортировать операции по дате? Да/Нет: ")).lower()
    if user_input_sort_by_date == "да":
        user_input_sort_reverse = str(input("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию: ")).lower()
        if user_input_sort_reverse == "по убыванию":
            result = (sort_by_date(filter_by_state_result))
        elif user_input_sort_reverse == "по возрастанию":
            result = (sort_by_date(filter_by_state_result,False))
    else:
        print ("Ну и всё тогда")

    user_input_sort_by_currency = str(input("Выводить только рублевые транзакции? Да/Нет: ")).lower()
    if user_input_sort_by_currency == "да":
        result = (find_rub_operations(sort_by_date(filter_by_state_result)))
    elif user_input_sort_by_currency == "нет":
        result = (sort_by_date(filter_by_state_result))
    else:
        print ("Что-то ты неправильное ввёл снова...")

    user_input_description_word = str(input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ")).lower()
    if user_input_description_word == "да":
        keyword = str(input("Введите слово по которому должен осуществляться поиск: ")).lower()
        result = (process_bank_search(find_rub_operations(sort_by_date(filter_by_state_result)), keyword))
    elif user_input_description_word == "нет":
        result = (find_rub_operations(sort_by_date(filter_by_state_result)))
    else:
        print("Что-то ты опять напутал... Видимо просто так стучишь по клавишам :)")

    return result




if __name__ == "__main__":
    print(use_app())