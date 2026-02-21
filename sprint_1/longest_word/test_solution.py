import pytest

from sprint_1.longest_word.solution import get_max_longest_word


@pytest.mark.parametrize(
    "words,expected",
    [
        ("i love segment tree", (2, 7)),
        (" i love segment tree", (2, 7)),
        ("   i love segment tree", (2, 7)),
        ("   i love segment              tree.   ", (2, 7)),
        (" i love segment tree ", (2, 7)),
        ("frog jumps from river", (1, 5)),
        ("i", (0, 1)),
        ("love love", (0, 4)),
        ("love s love", (0, 4)),
    ],
)
def test_simple(words, expected):
    assert get_max_longest_word(list(words.split())) == expected
