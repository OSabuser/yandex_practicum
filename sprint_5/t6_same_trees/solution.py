import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def are_twins(root1, root2):
    """
    Проверяет, являются ли два дерева близнецами.

    Деревья-близнецы имеют:
    - Одинаковую структуру
    - Одинаковые значения в соответствующих узлах

    Args:
        root1: корень первого дерева
        root2: корень второго дерева

    Returns:
        True если деревья идентичны, False иначе
    """
    # Базовый случай: оба узла пустые
    if root1 is None and root2 is None:
        return True

    # Один узел пустой, другой нет - не близнецы
    if root1 is None or root2 is None:
        return False

    # Оба узла существуют - проверяем значение и рекурсивно поддеревья
    return (
        root1.value == root2.value
        and are_twins(root1.left, root2.left)
        and are_twins(root1.right, root2.right)
    )


def solution(root1, root2) -> bool:
    return are_twins(root1, root2)


def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == "__main__":
    test()
