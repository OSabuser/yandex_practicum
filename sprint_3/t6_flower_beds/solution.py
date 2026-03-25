def get_task_date():
    gardeners = int(input())

    beds = []
    for _ in range(gardeners):
        beds.append(list(map(int, input().split())))

    return gardeners, beds


def get_beds_borders(gardeners, beds):
    result = []

    i = 0
    j = 0
    for _ in range(gardeners):
        pass


if __name__ == "__main__":
    gardeners, beds = get_task_date()
    print(f"Beds: {beds}")
