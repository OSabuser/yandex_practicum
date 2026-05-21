import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def remove_node(root, key):
    if root is None:
        return None

    if key < root.value:
        root.left = remove_node(root.left, key)
        return root

    if key > root.value:
        root.right = remove_node(root.right, key)
        return root

    # Нашли вершину для удаления
    if root.left is None:
        return root.right

    if root.right is None:
        return root.left

    # Оба ребенка есть:
    # берем самую правую вершину в левом поддереве
    pred_parent = root
    pred = root.left

    while pred.right is not None:
        pred_parent = pred
        pred = pred.right

    # Если pred — не непосредственный левый ребенок root,
    # нужно "подшить" левое поддерево pred к pred_parent.right
    if pred_parent != root:
        pred_parent.right = pred.left
        pred.left = root.left

    # В любом случае правое поддерево root становится правым поддеревом pred
    pred.right = root.right

    return pred


def remove(root, key) -> Node | None:
    return remove_node(root, key)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8


if __name__ == "__main__":
    test()
