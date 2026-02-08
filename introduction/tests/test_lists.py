import pytest

from src.main import zip_lists


@pytest.mark.parametrize(
    "length,list_1,list_2,expected",
    [
        (2, [1, 2], [2, 3, 4], None),
        (4, [1, 2, 3, 4], [5, 6, 7, 8], [1, 5, 2, 6, 3, 7, 4, 8]),
        (1, [1], [2], [1, 2]),
    ],
)
def test_zip(length, list_1, list_2, expected):
    assert zip_lists(length, list_1, list_2) == expected
    if expected is None:
        return
    assert length * 2 == len(expected)
