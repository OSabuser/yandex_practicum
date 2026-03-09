import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def get_node_by_index(head, index):
    while index:
        if head is None:
            break
        head = head.next_item
        index -= 1
    return head


# Получить значение узла ${node}
def get_node_value(node):
    if node is not None:
        return node.value


def get_index_by_value(head, value):
    index = 0
    while head is not None:
        node_value = get_node_value(head)
        if node_value is not None:
            if node_value == value:
                return index

        head = head.next_item
        index += 1

    return -1


def solution(node, elem):
    return get_index_by_value(node, elem)


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    idx = solution(node0, "node2")
    assert idx == 2

    idx = solution(node0, "node21")
    assert idx == -1


if __name__ == "__main__":
    test()
