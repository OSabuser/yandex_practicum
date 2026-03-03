import pytest

from sprint_2.t2_least_business.solution import (
    Node,
    del_node_by_index,
    get_node_by_index,
    get_node_value,
)


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


def test_get_node_by_index_returns_correct_value():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    result_1 = get_node_by_index(node0, 0)
    result_2 = get_node_by_index(node0, 1)
    result_3 = get_node_by_index(node0, 2)

    assert get_node_value(result_1) == "node0"
    assert get_node_value(result_2) == "node1"
    assert get_node_value(result_3) == "node2"

    result_wierd = get_node_by_index(node0, 15)
    assert get_node_value(result_wierd) is None


def test_del_head():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    # Удаление головы списка
    _result_1 = del_node_by_index(node0, 0)
    assert _result_1 is node1


def test_del_random():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    _result_1 = del_node_by_index(node0, 2)
    assert node1.next_item is node3


def test_del_last():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    _result_wierd = del_node_by_index(node0, 3)
    assert node2.next_item is None


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
