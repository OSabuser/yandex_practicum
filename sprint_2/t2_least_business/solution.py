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


def del_node_by_index(head, index):
    if head is None:
        return None

    # Удаляем голову списка, возвращаем новую
    if index == 0:
        return head.next_item

    # Получили узел, указывающий на удаляемый
    prev_node = get_node_by_index(head, index - 1)

    # Получили удаляемый узел
    temp_node = prev_node.next_item

    if temp_node is None:
        return head

    # Поменяли ссылку на следующий узел
    prev_node.next_item = temp_node.next_item

    return head


# Получить значение узла ${node}
def get_node_value(node):
    if node is not None:
        return node.value


# Отображение значений всех узлов списка, влоть до последнего
def solution(node, idx):
    return del_node_by_index(node, idx)


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == "__main__":
    test()
