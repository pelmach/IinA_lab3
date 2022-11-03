import lib
import pytest

# Тест сортировки пузерьком, функия которой принимает список чисел, возвращает его отсортированную копию
class TestSort:
    # Тестируем программу на корректных данных. Функция возвращает список элементов.
    def test_on_correction_n(self):
        assert lib.sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]