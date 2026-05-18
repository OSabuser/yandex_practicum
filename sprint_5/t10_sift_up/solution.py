def sift_up_iter(heap, idx):
    """
    Просеивание вверх в куче на максимум.

    Args:
        heap: массив, представляющий кучу (индексация с 1, heap[0] фиктивный)
        idx: индекс элемента, от которого начинается просеивание

    Returns:
        int: индекс, на котором элемент оказался после просеивания
    """
    # Поднимаемся вверх, пока не достигнем корня или не найдем правильное место
    while idx > 1:  # idx=1 это корень, выше подниматься некуда
        parent = idx // 2  # Индекс родителя

        # Если текущий элемент <= родителя, свойство кучи выполнено
        if heap[idx] <= heap[parent]:
            break

        # Меняем местами с родителем (текущий элемент больше)
        heap[idx], heap[parent] = heap[parent], heap[idx]

        # Продолжаем просеивание с позиции родителя
        idx = parent

    return idx


# Рекурсивная версия
def sift_up_recursive(heap, idx):
    """
    Рекурсивная версия просеивания вверх.
    """
    # Базовый случай: достигли корня
    if idx <= 1:
        return idx

    parent = idx // 2

    # Если нужна замена - меняем и продолжаем
    if heap[idx] > heap[parent]:
        heap[idx], heap[parent] = heap[parent], heap[idx]
        return sift_up_recursive(heap, parent)

    # Элемент на правильном месте
    return idx


def sift_up(heap, idx) -> int:
    return sift_up_recursive(heap, idx)


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == "__main__":
    test()
