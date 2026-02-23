import pytest

from sprint_1.binary_system.solution import get_sum


@pytest.mark.parametrize(
    "number1,number2,expected",
    [
        # Граничные случаи
        ("0", "0", "0"),
        ("1", "0", "1"),
        ("0", "1", "1"),
        ("1", "1", "10"),
        # Простые случаи
        ("101", "101", "1010"),
        ("101", "111", "1100"),
        ("1010", "1011", "10101"),
        ("1111", "1111", "11110"),
        # Сложные случаи
        ("1111111111111111", "0000000000000000", "1111111111111111"),
        ("1111111111111111", "0000000000000001", "10000000000000000"),
    ],
)
def test_simple(number1, number2, expected):
    assert get_sum(number1, number2) == expected
