def get_unsorted_array():
    length = int(input())
    array = list(map(int, input().split()))
    return length, array


def which_is_bigger(number_1, number_2):
    sa = str(number_1)
    sb = str(number_2)
    if sa + sb > sb + sa:
        return -1  # a перед b
    elif sa + sb < sb + sa:
        return 1  # b перед a
    else:
        return 0


def get_sorted_array(length, array, comparator=None):
    """Сортировка массива по неубыванию значения старшего разряда"""
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if comparator(array[j], array[j + 1]) == 1:
                # Меняем местами элементы (слева будет меньший)
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


if __name__ == "__main__":
    length, array = get_unsorted_array()
    array = get_sorted_array(length, array, which_is_bigger)
    print("".join(map(str, array)))
