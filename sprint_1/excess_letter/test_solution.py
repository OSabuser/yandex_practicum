import pytest

from sprint_1.excess_letter.solution import get_diff_char


@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("abcd", "abcde", "e"),
        ("go", "ogg", "g"),
        ("c", "cc", "c"),
        ("xtkpx", "xkctpx", "c"),
        ("aaaaaab", "aaaaaaba", "a"),
    ],
)
def test_simple(s1, s2, expected):
    assert get_diff_char(s1, s2) == expected
