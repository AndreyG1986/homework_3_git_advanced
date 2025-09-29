import pandas as pd


def read_xl_file(path_to_file_xl:str)->list:
    """Функция для считывания excel файла.
    должна принимать путь например:
    "../data/transactions_excel.xlsx"/"""
    transactions_excel_data = pd.read_excel(path_to_file_xl)
    # Преобразуем DataFrame в список словарей
    list_of_dicts_xl = transactions_excel_data.to_dict(orient='records')

    return list_of_dicts_xl

def read_csv_file(path_to_file_csv:str)->list:
    """Функция для считывания csv файла.
    должна принимать путь например:
    "../data/transactions.csv"/"""
    transactions_csv_data = pd.read_csv(path_to_file_csv)
    # Преобразуем DataFrame в список словарей
    list_of_dicts_csv = transactions_csv_data.to_dict(orient='records')

    return list_of_dicts_csv


if __name__ == "__main__":
    data_xl = read_xl_file("../data/transactions_excel.xlsx")
    print(data_xl[:2])
    data_csv = read_csv_file("../data/transactions.csv")
    print(data_csv[:2])