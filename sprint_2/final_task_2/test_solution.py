import pytest

from sprint_2.final_task_2.solution import MyDumbCalculator


@pytest.mark.parametrize(
    "numbers, expected",
    [
        (
            ["0", "-3", "4", "5"],
            [True, True, True, True],
        ),
        (
            ["a", "3a", "a4", "1231235"],
            [False, False, False, True],
        ),
        (
            ["0", "-0", "4-", "5"],
            [True, True, False, True],
        ),
    ],
)
def test_is_valid_operand(numbers, expected):
    assert len(numbers) == len(expected)
    for number, exp in zip(numbers, expected, strict=True):
        assert MyDumbCalculator.is_valid_operand(number) == exp


@pytest.mark.parametrize(
    "ops, expected",
    [
        (
            ["+", "-", "*", "/"],
            [True, True, True, True],
        ),
        (
            ["=", "++", "-_", ";"],
            [False, False, False, False],
        ),
    ],
)
def test_is_valid_operation(ops, expected):
    assert len(ops) == len(expected)
    for number, exp in zip(ops, expected, strict=True):
        assert MyDumbCalculator.is_valid_operation(number) == exp


@pytest.mark.parametrize(
    "expression, expected",
    [
        (
            "7 2 + 4 * 2 +",
            38,
        ),
        (
            "2 1 + 3 *",
            9,
        ),
        (
            "4 13 5 / +",
            6,
        ),
    ],
)
def test_is_correct_expression(expression, expected):
    calculator_sequence: list[str] = expression.split()

    calculator_instance = MyDumbCalculator()

    for element in calculator_sequence:
        if MyDumbCalculator.is_valid_operand(element):
            calculator_instance.store_number(int(element))
            continue
        if MyDumbCalculator.is_valid_operation(element):
            calculator_instance.perform_operation(element)

    assert calculator_instance.get_result() == expected
