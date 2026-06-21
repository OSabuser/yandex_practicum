def get_input() -> tuple[int, list[tuple[int, int]]]:
    """Считывает вместимость рюкзака и данные о кучах золота."""
    capacity = int(input())
    n = int(input())

    piles = []
    for _ in range(n):
        # c - цена за 1 кг, m - масса кучи
        c, m = map(int, input().split())
        piles.append((c, m))

    return capacity, piles


def solve_gold_rush(capacity: int, piles: list[tuple[int, int]]) -> int:
    """Жадный алгоритм для задачи о непрерывном рюкзаке."""
    # Сортируем кучи по цене за килограмм (первый элемент кортежа) по убыванию
    piles.sort(key=lambda x: x[0], reverse=True)

    total_value = 0

    for cost_per_kg, weight in piles:
        if capacity == 0:
            break  # Рюкзак забит под завязку

        # Берем либо всю кучу, если есть место, либо остаток вместимости
        weight_to_take = min(capacity, weight)

        # Добавляем стоимость взятого песка
        total_value += weight_to_take * cost_per_kg

        # Уменьшаем свободное место в рюкзаке
        capacity -= weight_to_take

    return total_value


if __name__ == "__main__":
    M, gold_piles = get_input()
    print(solve_gold_rush(M, gold_piles))
