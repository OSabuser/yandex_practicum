def get_unsorted_array():
    length = int(input())
    array = list(map(int, input().split()))
    return length, array


def get_sorted_array(length, array):
    # Проходим по всему массиву
    is_array_changed = False
    states = []
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                # Меняем местами элементы (слева будет меньший)
                array[j], array[j + 1] = array[j + 1], array[j]
                is_array_changed = True

        if is_array_changed:
            is_array_changed = False
            states.append(array.copy())
    return array, states


if __name__ == "__main__":
    length, array = get_unsorted_array()
    array, states = get_sorted_array(length, array)

    if len(states):
        for state in states:
            print(*state)
    else:
        print(*array)
