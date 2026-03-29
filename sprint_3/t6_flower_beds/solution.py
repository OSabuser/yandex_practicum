def get_task_data():
    gardeners = int(input())

    beds = []
    for _ in range(gardeners):
        beds.append(list(map(int, input().split())))

    return gardeners, beds


def sort_beds_by_borders(beds):
    # Сортируем список отрезков по началу, а при равном начале - по концу
    # по неубыванию
    beds.sort(key=lambda x: (x[0], x[1]))
    return beds


def get_merged_beds(beds):
    merged_beds = []
    for bed in beds:
        if merged_beds and merged_beds[-1][1] >= bed[0]:
            merged_beds[-1][1] = max(merged_beds[-1][1], bed[1])
        else:
            merged_beds.append(bed)
    return merged_beds


if __name__ == "__main__":
    gardeners, beds = get_task_data()
    sorted_beds = sort_beds_by_borders(beds)
    merged_beds = get_merged_beds(sorted_beds)
    for bed in merged_beds:
        print(f"{bed[0]} {bed[1]}")
