import pytest

from src.main import get_simple_moving_average_enhanced, get_simple_moving_average_naive


@pytest.mark.parametrize(
    "samples,list_1,window_size,expected",
    [
        (7, [1, 2, 3, 4, 5, 6, 7], 4, [2.5, 3.5, 4.5, 5.5]),
        (5, [1, 2, 3, 4, 5], 5, [3.0]),
        (4, [1, 2, 3], 2, None),
    ],
)
def test_average(samples, list_1, window_size, expected):
    assert get_simple_moving_average_naive(samples, list_1, window_size) == expected
    assert get_simple_moving_average_enhanced(samples, list_1, window_size) == expected
