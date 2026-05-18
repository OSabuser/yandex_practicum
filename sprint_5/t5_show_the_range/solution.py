import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


# Оптимизированная версия с отсечением
def print_range_optimized(root, L, R):
    """
    Оптимизированная версия с отсечением поддеревьев.
    Работает корректно даже если дубликаты могут быть где угодно.
    """
    result = []

    def inorder_range(node):
        if node is None:
            return

        # Left - заходим только если возможны значения >= L
        # В левом поддереве все значения <= node.value
        # Заходим если node.value >= L (там могут быть нужные значения)
        if node.value >= L:
            inorder_range(node.left)

        # Middle
        if L <= node.value <= R:
            result.append(node.value)

        # Right - заходим только если возможны значения <= R
        # В правом поддереве все значения >= node.value
        # Заходим если node.value <= R (там могут быть нужные значения)
        if node.value <= R:
            inorder_range(node.right)

    inorder_range(root)
    print(" ".join(map(str, result)))


def print_range(node, l, r):
    print_range_optimized(node, l, r)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == "__main__":
    test()
