import pytest

from sprint_1.power_of_four.solution import is_number_a_power_of_four


@pytest.mark.parametrize(
    "number,expected",
    [
        # Граничные случаи
        (1, "True"),
        (10000, "False"),
        # Степени двойки
        (2, "False"),
        (4, "True"),
        (8, "False"),
        (16, "True"),
        (32, "False"),
        (64, "True"),
        (128, "False"),
        (256, "True"),
        (512, "False"),
        (1024, "True"),
        # Степени двойки минус 1
        (3, "False"),
        (7, "False"),
        (15, "False"),
        (31, "False"),
        (63, "False"),
    ],
)
def test_simple(number, expected):
    assert is_number_a_power_of_four(number) == expected
