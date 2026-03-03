import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        # Длина связного списка (предполагается что список может существовать
        # в единственном экземпляре)
        __list_length: int = 0

        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item
            Node.__list_length += 1

        def __del__(self):
            Node.__list_length -= 1

        @classmethod
        def get_list_length(cls) -> int:
            return cls.__list_length


# Отображение значений всех узлов списка, влоть до последнего
def solution(node):
    while node:
        data = get_node_value(node)
        print(data)
        node = node.next_item


# Получить значение узла ${node}
def get_node_value(node):
    if node is not None:
        return node.value


def test():
    node3 = Node("node3", None)
    print(f"List's length: {Node.get_list_length()}")
    node2 = Node("node2", node3)
    print(f"List's length: {Node.get_list_length()}")
    node1 = Node("node1", node2)
    print(f"List's length: {Node.get_list_length()}")
    node0 = Node("node0", node1)
    print(f"List's length: {Node.get_list_length()}")
    solution(node0)
    print()
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == "__main__":
    test()
