def filter_by_state(users_info_list: list, state: str = "EXECUTED") -> list:
    """функция, которая принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те
    словари, у которых ключ state соответствует указанному значению."""
    # создаём пустой список
    state_list = []
    # начинаем перебирать словари
    for item in users_info_list:
        # используем метод get и создаём переменную state,
        # чтобы иметь доступ к значениям словаря
        state_data = item.get("state")
        # если значение ключа "state" == 'EXECUTED'
        # и мы хотим сортировать список, то
        # добавляем данный словарь в список state_executed
        if state == state_data:
            state_list.append(item)

    return state_list


def sort_by_date(users_info_list: list, parameter_sort_reverse: bool = True) -> list:
    """функция sort_by_date, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список,
    отсортированный по дате (date)."""
    date = ""
    sorted_users_info_list = []
    # начинаем перебирать словари
    for item in users_info_list:
        # используем метод индекс и создаём переменную index,
        # чтобы иметь доступ к элементам списка
        index = users_info_list.index(item)
        # используем метод get и создаём переменную date,
        # чтобы иметь доступ к значениям словаря
        date = users_info_list[index].get("date")
        # - `key=lambda x: x['date']` — здесь мы используем анонимную функцию
        # `lambda`, которая говорит `sorted()`,
        # что сортировать нужно по значению ключа `'date'` в каждом словаре.
        if parameter_sort_reverse == True:
            sorted_users_info_list = sorted(users_info_list, key=lambda x: x["date"], reverse=True)
        else:
            sorted_users_info_list = sorted(users_info_list, key=lambda x: x["date"])

    return sorted_users_info_list
