import lib
import pytest

# Тест определения n чисел Фибоначчи – функция принимает n, возвращает список из чисел
class TestFib:

    # Тестируем программу на корректных данных. Функция возвращает список элементов.
    def test_on_correction_n(self):
        assert lib.fibonacci(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    # Тестируем программу на некорруктных данных. Функция вызывает исключение IndexError. // работает не правильно
    # Функия по дефолту вывод [1, 1] при вводе некорректных данных

    def test_on_uncorrection_n(self):
        with pytest.raises(IndexError):
            lib.fibonacci(0)
