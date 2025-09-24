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


def log(filename=None):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Если всё правильно, то выполняем то, что в try
            try:
                result = func(*args, **kwargs)
            # Если ошибка выполняется то что в except
            except Exception as e:
                msg = f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                raise e
            # В противном случае отправляем в консоль сообщение
            else:
                msg = f"{func.__name__} ok"
            # Если filename задан, то выполняется finally
            finally:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{msg}\n")
                else:
                    print(msg)

        return wrapper

    return inner


@log("my_log.txt")
# @log()
def summator(a, b):
    return a + b


if __name__ == "__main__":
    print(summator(7, 5))
