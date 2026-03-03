import pytest

from sprint_2.t1_todo_list.solution import Node, get_node_value


@pytest.mark.parametrize(
    "node, expected",
    [
        (Node("node0"), "node0"),
        (Node(42), 42),
        (Node(None), None),
        (Node(3.14), 3.14),
        (Node("hello", Node("world")), "hello"),
    ],
)
def test_get_node_value_returns_correct_value(node, expected):
    assert get_node_value(node) == expected


def test_get_node_value_with_none_returns_none():
    assert get_node_value(None) is None


def test_get_node_value_does_not_advance_to_next():
    node2 = Node("second")
    node1 = Node("first", node2)
    assert get_node_value(node1) == "first"


def test_get_node_value_single_node_chain():
    node = Node("only")
    assert get_node_value(node) == "only"
    assert node.next_item is None
