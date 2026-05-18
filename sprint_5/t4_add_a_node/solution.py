import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if not LOCAL:
    from node import Node

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert_node(root, value):
    if root is None:
        return Node(value=value)

    if value < root.value:
        root.left = insert_node(root.left, value)
    elif value >= root.value:
        root.right = insert_node(root.right, value)

    return root


def insert(root, key) -> Node:
    return insert_node(root, key)


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == "__main__":
    test()
