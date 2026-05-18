import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def is_mirror(left_node, right_node):
    """
    Проверяет, являются ли два поддерева зеркальными отражениями.

    Args:
        left_node: корень левого поддерева
        right_node: корень правого поддерева

    Returns:
        True если поддеревья зеркальны, False иначе
    """
    # Оба узла пустые - зеркальны
    if left_node is None and right_node is None:
        return True

    # Один узел пустой, другой нет - не зеркальны
    if left_node is None or right_node is None:
        return False

    # Проверяем:
    # 1. Значения совпадают
    # 2. Левое поддерево left_node зеркально правому поддереву right_node
    # 3. Правое поддерево left_node зеркально левому поддереву right_node
    return (
        left_node.value == right_node.value
        and is_mirror(left_node.left, right_node.right)
        and is_mirror(left_node.right, right_node.left)
    )


def is_anagram_tree(root):
    """
    Определяет, является ли дерево анаграммой (симметричным).

    Args:
        root: корень дерева

    Returns:
        True если дерево симметрично, False иначе
    """
    # Пустое дерево считается симметричным
    if root is None:
        return True

    # Проверяем, зеркальны ли левое и правое поддеревья
    return is_mirror(root.left, root.right)


def solution(root) -> bool:
    return is_anagram_tree(root)


def test():
    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)


if __name__ == "__main__":
    test()
