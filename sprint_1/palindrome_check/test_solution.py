import pytest

from sprint_1.palindrome_check.solution import is_word_palindrome


@pytest.mark.parametrize(
    "text,expected",
    [
        ("madam", True),
        ("racecar", True),
        ("hello", False),
        ("a", False),
        ("aa", True),
        ("ab", False),
        ("A man a plan a canal Panama", True),
        ("Was it a car or a cat I saw", True),
        ("No lemon no melon", True),
        ("not a palindrome", False),
        ("12321", True),
        ("12345", False),
    ],
)
def test_simple(text, expected):
    assert is_word_palindrome(text.lower()) == expected
