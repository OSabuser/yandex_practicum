import pytest

from sprint_1.lucky_numbers import (
    make_decision,
)


@pytest.mark.parametrize(
    "values,expected",
    [
        ([-8, -5, -2, 7], "ERROR"),
        (
            [
                -8,
                -5,
            ],
            "ERROR",
        ),
        (
            [
                -5,
            ],
            "ERROR",
        ),
        (
            [8, 2, 9],
            "FAIL",
        ),
        ([2, 4, 6], "WIN"),
        ([0, 0, 0], "WIN"),
        ([0, 1, 0], "FAIL"),
        ([-1, -1, -1], "WIN"),
        ([-2, -4, -6], "WIN"),
    ],
)
def test_simple(values, expected):
    assert make_decision(values) == expected


@pytest.mark.parametrize(
    "a,expected",
    [
        ("-8 -5 -2 7", "ERROR"),
        ("\r\n1 2  3\r\n", "FAIL"),
        ("7 11 13", "WIN"),
        ("2000 10000000 2", "WIN"),
        ("2000000000 1 0", "ERROR"),
        ("0 0 0", "WIN"),
        ("0 1 0", "FAIL"),
    ],
)
def test_complicated(a, expected):
    values = list(map(int, a.split()))
    assert make_decision(values) == expected
