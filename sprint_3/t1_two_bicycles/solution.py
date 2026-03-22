def get_task_data():
    days = int(input())
    savings = list(map(int, input().split()))
    bicycle_cost = int(input())
    return days, savings, bicycle_cost


def binarySearch(arr, x, left, right):
    """Взято из теоретической части Практикума"""
    if left >= right:  # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] >= x:
        # ищем, нет ли подходящего дня левее
        left_answer = binarySearch(arr, x, left, mid)

        return mid if left_answer == -1 else left_answer
    elif x < arr[mid]:  # искомый элемент меньше центрального значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else:  # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)


if __name__ == "__main__":
    days, savings, bicycle_cost = get_task_data()
    index_0 = binarySearch(savings, bicycle_cost, left=0, right=days)
    index_1 = binarySearch(savings, 2 * bicycle_cost, left=0, right=days)
    # Переход с индексной нотации к номеру дня
    index_0 = index_0 + 1 if index_0 != -1 else -1
    index_1 = index_1 + 1 if index_1 != -1 else -1
    print(f"{index_0} {index_1}")
