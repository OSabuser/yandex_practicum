import pytest

from sprint_1.func_value import (
    get_func_value,
)


@pytest.mark.parametrize(
    "a,x,b,c,expected",
    [
        (-8, -5, -2, 7, -183),
        (8, 2, 9, -10, 40),
        (0, 0, 0, 7, 7),
        (1, 5, 1, 0, 30),
    ],
)
def test_simple(a, x, b, c, expected):
    assert get_func_value(a, x, b, c) == expected


@pytest.mark.parametrize(
    "a,expected",
    [
        ("-8 -5 -2 7", -183),
        ("\r\n8       2 9   -10\r\n", 40),
        ("0 0 0 0", 0),
        ("1 7 1 0", 56),
    ],
)
def test_complicated(a, expected):
    a, x, b, c = map(int, a.split())
    assert get_func_value(a, x, b, c) == expected
