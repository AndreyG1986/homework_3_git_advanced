def filter_by_state(users_info_list: list, state:str = 'EXECUTED', parameter_sort:bool = True) ->list:
    """функция, которая принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те
    словари, у которых ключ state соответствует указанному значению."""
    # создаём пустой список
    state_list = []
    # начинаем перебирать словари
    for item in users_info_list:
        # используем метод индекс и создаём переменную index,
        # чтобы иметь доступ к элементам списка
        index = users_info_list.index(item)
        # используем метод get и создаём переменную state,
        # чтобы иметь доступ к значениям словаря
        state_ = users_info_list[index].get('state')
        # если значение ключа "state" == 'EXECUTED'
        # и мы хотим сортировать список, то
        # добавляем данный словарь в список state_executed
        if state == state_ and parameter_sort == True:
            state_list.append(users_info_list[index])

    return state_list


def sort_by_date(users_info_list: list) -> list:
    """ функция sort_by_date, которая принимает список словарей и необязательный параметр,
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
        date = users_info_list[index].get('date')
        #- `key=lambda x: x['date']` — здесь мы используем анонимную функцию
        # `lambda`, которая говорит `sorted()`,
        # что сортировать нужно по значению ключа `'date'` в каждом словаре.
        sorted_users_info_list = sorted(
            users_info_list, key=lambda x: x['date'], reverse=True
            )

    return sorted_users_info_list