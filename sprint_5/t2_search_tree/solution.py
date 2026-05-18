import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


# Центрированный обход дерева: LMR
def is_tree_valid(root):
    """Проверяет, является ли дерево бинарным деревом поиска."""
    state = {"is_valid": True, "prev_value": None}

    def inorder_validate(root):
        if root is None or not state["is_valid"]:
            return

        # Left - обрабатываем левое поддерево
        inorder_validate(root.left)

        # Middle - проверяем текущий узел
        if state["prev_value"] is not None and root.value <= state["prev_value"]:
            state["is_valid"] = False
            return

        state["prev_value"] = root.value

        # Right - обрабатываем правое поддерево
        inorder_validate(root.right)

    inorder_validate(root)

    return state["is_valid"]


def solution(root) -> bool:
    return is_tree_valid(root)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == "__main__":
    test()
