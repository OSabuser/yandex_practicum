import pytest

from sprint_1.remote_work.solution import get_str_bin_representation


@pytest.mark.parametrize(
    "number,expected",
    [
        # Граничные случаи
        (0, "0"),
        (1, "1"),
        (10000, "10011100010000"),
        # Степени двойки
        (2, "10"),
        (4, "100"),
        (8, "1000"),
        (16, "10000"),
        (32, "100000"),
        (64, "1000000"),
        (128, "10000000"),
        (256, "100000000"),
        (512, "1000000000"),
        (1024, "10000000000"),
        # Степени двойки минус 1
        (3, "11"),
        (7, "111"),
        (15, "1111"),
        (31, "11111"),
        (63, "111111"),
        (127, "1111111"),
        (255, "11111111"),
        # Обычные числа
        (5, "101"),
        (10, "1010"),
        (42, "101010"),
        (100, "1100100"),
        (255, "11111111"),
        (1000, "1111101000"),
        (2021, "11111100101"),
        (5000, "1001110001000"),
        (9999, "10011100001111"),
    ],
)
def test_simple(number, expected):
    assert get_str_bin_representation(number) == expected


@pytest.mark.parametrize(
    "number,expected",
    [
        # Проверка что результат можно преобразовать обратно
        (42, "101010"),
        (255, "11111111"),
        (1024, "10000000000"),
        # Проверка различных диапазонов
        (7, "111"),
        (77, "1001101"),
        (777, "1100001001"),
        (7777, "1111001100001"),
        # Последовательные числа для проверки корректности
        (10, "1010"),
        (11, "1011"),
        (12, "1100"),
        (13, "1101"),
        (14, "1110"),
        (15, "1111"),
        (16, "10000"),
    ],
)
def test_conversion_correctness(number, expected):
    """Проверяем что преобразование корректно и результат можно преобразовать обратно"""
    result = get_str_bin_representation(number)
    assert result == expected
    # Проверяем что результат является валидным двоичным числом
    assert all(c in "01" for c in result)
    # Проверяем что преобразование обратно в десятичную систему дает исходное число
    assert int(result, 2) == number


@pytest.mark.parametrize(
    "number",
    [0, 1, 2, 10, 50, 100, 500, 1000, 5000, 9999, 10000],
)
def test_no_leading_zeros(number):
    """Проверяем что в результате нет ведущих нулей (кроме числа 0)"""
    result = get_str_bin_representation(number)
    if number == 0:
        assert result == "0"
    else:
        assert result[0] == "1", f"Результат для {number} не должен начинаться с 0"


@pytest.mark.parametrize(
    "number",
    [0, 1, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191],
)
def test_powers_of_two_minus_one(number):
    """Проверяем числа вида 2^n - 1 (все биты единицы)"""
    result = get_str_bin_representation(number)
    if number == 0:
        assert result == "0"
    else:
        assert all(c == "1" for c in result), f"Для {number} все биты должны быть 1"
