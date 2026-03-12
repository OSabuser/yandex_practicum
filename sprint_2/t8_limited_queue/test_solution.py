import pytest

from sprint_2.t8_limited_queue.solution import MyQueueSized


@pytest.mark.parametrize(
    "queue_size, command, expected",
    [
        (0, "pussdfh 1", None),
        (1, "push 1", None),
        (14, "pop", "None"),
        (0, "peek", "None"),
    ],
)
def test_run_one_user_command(queue_size, command, expected):
    queue = MyQueueSized(queue_size)
    assert queue.run_user_command(command) == expected


@pytest.mark.parametrize(
    "total_commands, queue_size, commands, expected",
    [
        (
            4,
            1,
            ["push 1", "peek", "pop", "peek"],
            [None, 1, 1, "None"],
        ),
        (
            8,
            2,
            ["peek", "push 5", "push 2", "peek", "size", "size", "push 1", "size"],
            ["None", None, None, 5, 2, 2, "error", 2],
        ),
        (
            10,
            1,
            [
                "push 1",
                "size",
                "push 3",
                "size",
                "push 1",
                "pop",
                "push 1",
                "pop",
                "push 3",
                "push 3",
            ],
            [None, 1, "error", 1, "error", 1, None, 1, None, "error"],
        ),
    ],
)
def test_run_command_sequence(total_commands, queue_size, commands, expected):
    assert len(commands) == total_commands
    assert len(expected) == total_commands
    queue = MyQueueSized(queue_size)
    for cmd, exp in zip(commands, expected, strict=True):
        assert queue.run_user_command(cmd) == exp
