import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def is_balanced(root):
    """
    Определяет, является ли дерево сбалансированным.

    Дерево сбалансировано, если для каждой вершины высоты
    левого и правого поддеревьев отличаются не более чем на 1.

    Args:
        root: корень дерева

    Returns:
        True если дерево сбалансировано, False иначе
    """

    def check_height(node):
        """
        Возвращает высоту дерева, если оно сбалансировано.
        Возвращает -1, если дерево НЕ сбалансировано.

        Returns:
            int: высота дерева или -1 если не сбалансировано
        """
        # Базовый случай: пустое дерево имеет высоту 0 и сбалансировано
        if node is None:
            return 0

        # Рекурсивно проверяем левое поддерево
        left_height = check_height(node.left)
        if left_height == -1:  # Левое поддерево не сбалансировано
            return -1

        # Рекурсивно проверяем правое поддерево
        right_height = check_height(node.right)
        if right_height == -1:  # Правое поддерево не сбалансировано
            return -1

        # Проверяем балансировку текущего узла
        if abs(left_height - right_height) > 1:
            return -1  # Текущий узел не сбалансирован

        # Возвращаем высоту текущего поддерева
        return max(left_height, right_height) + 1

    # Дерево сбалансировано, если check_height не вернула -1
    return check_height(root) != -1


def solution(root) -> bool:
    return is_balanced(root)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == "__main__":
    test()
