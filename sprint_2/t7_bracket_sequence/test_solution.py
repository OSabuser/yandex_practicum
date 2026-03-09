import pytest

from sprint_2.t7_bracket_sequence.solution import Stack, is_correct_bracket_seq


def test_pop_item_from_empty_stack():
    user_stack = Stack()
    assert user_stack.pop() == "error"


def test_get_stacks_max_item_value_from_empty_stack():
    user_stack = Stack()
    assert user_stack.get_max() == "None"


@pytest.mark.parametrize(
    "sequence, expected",
    [
        ("", True),
        ("}{", False),
        ("{}", True),
        ("{[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]}", True),
        ("{[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]}", False),
        ("{]", False),
        ("{[}]", False),
    ],
)
def test_get_node_value_returns_correct_value(sequence, expected):
    assert is_correct_bracket_seq(sequence) == expected
