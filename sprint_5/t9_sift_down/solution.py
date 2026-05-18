# Рекурсивная версия (альтернатива)
def sift_down_recursive(heap, idx):
    """
    Рекурсивная версия просеивания вниз.
    """
    n = len(heap) - 1
    largest = idx
    left = 2 * idx
    right = 2 * idx + 1

    # Находим максимальный среди текущего узла и его детей
    if left <= n and heap[left] > heap[largest]:
        largest = left

    if right <= n and heap[right] > heap[largest]:
        largest = right

    # Если нужна замена - меняем и продолжаем
    if largest != idx:
        heap[idx], heap[largest] = heap[largest], heap[idx]
        return sift_down_recursive(heap, largest)

    return idx


def _sift_down_iter(heap, idx):
    """
    Просеивание вниз в куче на максимум.

    Args:
        heap: массив, представляющий кучу (индексация с 1, heap[0] фиктивный)
        idx: индекс элемента, от которого начинается просеивание

    Returns:
        int: индекс, на котором элемент оказался после просеивания
    """
    n = len(heap) - 1  # Реальный размер кучи (без фиктивного элемента)

    while True:
        largest = idx  # Изначально считаем текущий элемент максимальным
        left = 2 * idx  # Индекс левого ребёнка
        right = 2 * idx + 1  # Индекс правого ребёнка

        # Проверяем левого ребёнка
        if left <= n and heap[left] > heap[largest]:
            largest = left

        # Проверяем правого ребёнка
        if right <= n and heap[right] > heap[largest]:
            largest = right

        # Если текущий элемент уже максимален среди себя и детей - готово
        if largest == idx:
            break

        # Меняем местами с максимальным ребёнком
        heap[idx], heap[largest] = heap[largest], heap[idx]

        # Продолжаем просеивание с новой позиции
        idx = largest

    return idx


def sift_down(heap, idx) -> int:
    return sift_down_recursive(heap, idx)


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == "__main__":
    test()
