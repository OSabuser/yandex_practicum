import pytest

from sprint_1.final_task_2.solution import get_max_points_value, get_numbers_occurences


@pytest.mark.parametrize(
    "field_str,expected",
    [
        ("................", [0, 0, 0, 0, 0, 0, 0, 0, 0]),
        ("1...............", [1, 0, 0, 0, 0, 0, 0, 0, 0]),
        (".......2........", [0, 1, 0, 0, 0, 0, 0, 0, 0]),
        ("...............9", [0, 0, 0, 0, 0, 0, 0, 0, 1]),
        ("1.3.5.7.9.1.3.5", [2, 0, 2, 0, 2, 0, 1, 0, 1]),
        ("9999999999999999", [0, 0, 0, 0, 0, 0, 0, 0, 16]),
        ("123456789.......", [1, 1, 1, 1, 1, 1, 1, 1, 1]),
        ("1212134343455555", [3, 2, 3, 3, 5, 0, 0, 0, 0]),
    ],
)
def test_occurrences(field_str, expected):
    assert get_numbers_occurences(field_str) == expected


@pytest.mark.parametrize(
    "free_fingers,field_str,expected",
    [
        (5, "................", 0),
        (2, "123456789.......", 9),
        (6, "1212134343455555", 5),
        (2, "1212134343455555", 1),
    ],
)
def test_points(free_fingers, field_str, expected):
    assert get_max_points_value(free_fingers, field_str) == expected
