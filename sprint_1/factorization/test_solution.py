import pytest

from sprint_1.factorization.solution import factorize


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, []),
        (2, [2]),
        (8, [2, 2, 2]),
        (9, [3, 3]),
        (10, [2, 5]),
        (12, [2, 2, 3]),
        (13, [13]),
        (14, [2, 7]),
        (100, [2, 2, 5, 5]),
    ],
)
def test_simple(number, expected):
    assert factorize(number) == expected
