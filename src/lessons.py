from functools import reduce, wraps
from time import perf_counter, sleep


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        stop = perf_counter()
        result_time = stop - start
        print(f"{func.__name__} выполнилась за {result_time: 5f}")
        return result

    return wrapper


def slowit(seconds):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            sleep(seconds)

            return result

        return wrapper

    return inner


# Без кеширования время работы функции при каждом вызове не менее 2 секунд.
@timeit
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n + 1)) if n > 0 else None


print(product(10))
print(product(10))


def memoize(func):
    cash = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cash:
            result = func(*args, **kwargs)
            cash[args] = result
        else:
            result = cash[args]
        return result

    return wrapper


# С кешированием время работы функции при первом вызове не менее 2 секунд, при втором вызове почти мгновенно.
@timeit
@memoize
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n + 1)) if n > 0 else None


print(product(10))
print(product(10))
