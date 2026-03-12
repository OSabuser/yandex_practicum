import pytest

from sprint_2.t9_list_queue.solution import MyLinkedQueue


@pytest.mark.parametrize(
    "command, expected",
    [
        ("put 1", None),
        ("get", "error"),
        ("size", 0),
    ],
)
def test_run_one_user_command(command, expected):
    queue = MyLinkedQueue()
    assert queue.run_user_command(command) == expected


@pytest.mark.parametrize(
    "total_commands, commands, expected",
    [
        (
            5,
            ["get", "put 11414", "size", "get", "size"],
            ["error", None, 1, 11414, 0],
        ),
        (
            10,
            ["put -34", "put -23", "get", "size", "get", "size", "get", "get", "put 80", "size"],
            [
                None,
                None,
                -34,
                1,
                -23,
                0,
                "error",
                "error",
                None,
                1,
            ],
        ),
        (
            6,
            ["put -66", "put 98", "size", "size", "get", "get"],
            [
                None,
                None,
                2,
                2,
                -66,
                98,
            ],
        ),
    ],
)
def test_run_command_sequence(total_commands, commands, expected):
    assert len(commands) == total_commands
    assert len(expected) == total_commands
    queue = MyLinkedQueue()
    for cmd, exp in zip(commands, expected, strict=True):
        assert queue.run_user_command(cmd) == exp
