def get_input_values():
    length_of_street = int(input())
    house_numbers = list(map(int, input().split()))
    return length_of_street, house_numbers


def get_closest_distances(length, houses):
    distances = [length + 1] * length

    # Записываем индексы незанятых домов (т.н. нули)
    current_zero = length + 1
    for house_index in range(length):
        if houses[house_index] == 0:
            current_zero = house_index

        distances[house_index] = house_index - current_zero

    print(f"Current distance: {distances}")
    # Переворачиваем массив и проходимся по нему еще раз в обратную сторону
    current_zero = length + 1
    for house_index in range(length - 1, -1, -1):
        if houses[house_index] == 0:
            current_zero = house_index
        print(f"{current_zero - house_index} или {distances[house_index]}")

    return distances


if __name__ == "__main__":
    length_of_street, house_numbers = get_input_values()

    print(*get_closest_distances(length_of_street, house_numbers))
