import pytest

from sprint_2.final_task_1.solution import MyDequeueSized


@pytest.mark.parametrize(
    "queue_size, command, expected",
    [
        (0, "pussdfh 1", None),
        (1, "push 1", None),
        (14, "pop_back", "error"),
        (0, "push_back 4", "error"),
        (1, "push_back 4", None),
    ],
)
def test_run_one_user_command(queue_size, command, expected):
    queue = MyDequeueSized(queue_size)
    assert queue.run_user_command(command) == expected


@pytest.mark.parametrize(
    "total_commands, queue_size, commands, expected",
    [
        (
            5,
            1,
            ["push_back 14", "pop_front", "pop_back", "push_back 1", "push_back 1"],
            [None, 14, "error", None, "error"],
        ),
        (
            6,
            6,
            [
                "push_front -201",
                "push_back 959",
                "push_back 102",
                "push_front 20",
                "pop_front",
                "pop_back",
            ],
            [None, None, None, None, 20, 102],
        ),
        (
            7,
            10,
            [
                "push_front -855",
                "push_front 0",
                "pop_back",
                "pop_back",
                "push_back 844",
                "pop_back",
                "push_back 823",
            ],
            [None, None, -855, 0, None, 844, None],
        ),
    ],
)
def test_run_command_sequence(total_commands, queue_size, commands, expected):
    assert len(commands) == total_commands
    assert len(expected) == total_commands
    queue = MyDequeueSized(queue_size)
    for cmd, exp in zip(commands, expected, strict=True):
        assert queue.run_user_command(cmd) == exp
