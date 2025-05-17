import pytest
from time import time
from src.decorators import log, timer


@log
def multiplier(x, y):
    return x * y


def test_log(capsys):
    multiplier(3, 5)
    captured = capsys.readouterr()
    assert captured.out == "Function multiplier started\nФункция multiplier дала результат 15\nFunction multiplier finished\n"

def test_log_error():
    with pytest.raises(ValueError, match="All arguments must be positive integers"):
        multiplier(3, 0)


# Не знаю как протестировать время
# @timer
# def timer(func):
#     pass
