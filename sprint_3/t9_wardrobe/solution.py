def sort_items_by_color(items, colors_count):
    """Из теории спринта №3"""
    counted_values = [0] * colors_count
    for value in items:
        counted_values[value] += 1

    index = 0
    for value in range(colors_count):
        for _ in range(counted_values[value]):
            items[index] = value
            index += 1
    return items


def get_wardrobe_clothes():
    items = int(input())
    clothes = list(map(int, input().split()))
    return items, clothes


_TYPE_OF_COLORS = 3
if __name__ == "__main__":
    items, clothes = get_wardrobe_clothes()
    sort_items_by_color(clothes, _TYPE_OF_COLORS)
    print(*clothes)
