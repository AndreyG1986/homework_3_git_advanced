import time
from functools import wraps
from time import time


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Данная функция создана для изменения результата другой функции
        (входящей сюда в качестве аргумента)"""
        print(f"Function {func.__name__} started")
        for arg in args or kwargs:
            if arg <= 0:
                raise ValueError("All arguments must be positive integers")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} дала результат {result}")
        print(f"Function {func.__name__} finished")
        return result

    return wrapper


# Пример из курса
# def printing(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs) :
#           print(f'Function {func} started')
#           result = func(*args, **kwargs)
#           print(f'Function {func} finished')
#           return result
#     return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Данная функция создана для подсчёта времени, которое будет затрачено на
        обработку декоратора log"""
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        print(f"Time for work: {time_2 - time_1}")
        return result

    return wrapper


@timer
@log
def multiplier(a, b):
    return a * b


if __name__ == "__main__":
    print(multiplier(3, 5))

# def example():
#     for i in range (100000000):
#         continue
#
# example()

# Напишите декоратор, который повторно вызывает декорируемую функцию
# заданное количество раз через заданное время,
# если произошла ошибка. Параметры, передаваемые в декоратор,
# обязательно должны быть именованными.


# def retry(*, retries=3, delay=3):
#     def wrapper(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             for i in range(retries):
#                 try:
#                     return func(*args, **kwargs)
#                 except:
#                     time.sleep(delay)
#             raise Exception('Function call failed after multiple retries.')
#         return inner
#     return wrapper

def log(filename=None):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"Ошибка в {func.__name__}: {e}. Входные данные: {args}, {kwargs}\n")
                else:
                    print(f"Ошибка в {func.__name__}: {e}. Входные данные: {args}, {kwargs}")
                raise
            else:
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"Функция {func.__name__} ок. Результат {result}\n")
                else:
                    print(f"Функция {func.__name__} ок. Результат {result}")
                return result
        return wrapper
    return inner

# @log('my_log.txt')
@log()
def summator(a, b):
    return a + b

# result = summator(2, 5)

# ну и тут по идее должны что-то проверить, но пока ничего не работает
if __name__ == "__main__":
    print(summator(1, 5))