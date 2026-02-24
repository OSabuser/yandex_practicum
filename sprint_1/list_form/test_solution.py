import pytest

from sprint_1.list_form.solution import get_sum


@pytest.mark.parametrize(
    "len1,list_form1,list_form2,expected",
    [
        # Граничные случаи
        (1, [1], [0], [1]),
        (1, [0], [0], [0]),
        (1, [0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]),
        (5, [9, 9, 9, 9, 9], [1, 0, 0, 0, 0], [1, 0, 9, 9, 9, 9]),
        (5, [9, 9, 9, 9, 9], [1], [1, 0, 0, 0, 0, 0]),
        (4, [1, 2, 0, 0], [3, 4], [1, 2, 3, 4]),
    ],
)
def test_simple(len1, list_form1, list_form2, expected):
    assert get_sum(len1, list_form1, list_form2) == expected
