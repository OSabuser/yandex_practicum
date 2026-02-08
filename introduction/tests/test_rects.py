import pytest

from src.main import calculate_possible_rects


@pytest.mark.parametrize(
    "rectw,recth,w, h, expected",
    [
        (640, 480, 64, 48, 0),
        (640, 480, 64, 48, 0),
    ],
)
def test_rect(rectw, recth, w, h, expected):
    assert calculate_possible_rects(rectw, recth, w, h) == expected
