def merge(arr, lf, mid, rg):
    """Сливает два отсортированных подмассива arr[lf:mid] и arr[mid:rg]
    в один отсортированный подмассив arr[begin:end] (на месте)."""
    left_ptr = lf  # текущий индекс в левой половине
    right_ptr = mid  # текущий индекс в правой половине
    result = []  # временный буфер

    # основное слияние двух отсортированных половин
    while left_ptr < mid and right_ptr < rg:
        if arr[left_ptr] <= arr[right_ptr]:
            result.append(arr[left_ptr])
            left_ptr += 1
        else:
            result.append(arr[right_ptr])
            right_ptr += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий:

    # «хвост» левой половины
    while left_ptr < mid:
        result.append(arr[left_ptr])
        left_ptr += 1

    # «хвост» правой половины
    while right_ptr < rg:
        result.append(arr[right_ptr])
        right_ptr += 1

    return result


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:  # базовый случай рекурсии
        return

    # определяем середину
    middle = (lf + rg) // 2

    # запускаем сортировку рекурсивно на левой половине
    merge_sort(arr, lf, middle)

    # запускаем сортировку рекурсивно на правой половине
    merge_sort(arr, middle, rg)

    # формируем in-place слияние
    merged = merge(arr, lf, middle, rg)
    arr[lf:rg] = merged


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == "__main__":
    test()
