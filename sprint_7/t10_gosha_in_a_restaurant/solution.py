def get_input() -> tuple[int, list[int]]:
    """Считывает количество дней и цены обедов."""
    n = int(input().strip())
    # Считываем n строк с ценами
    prices = [int(input().strip()) for _ in range(n)]
    return n, prices


def solve_restaurant(n: int, prices: list[int]) -> tuple[int, int, list[int]]:
    """ДП для поиска минимальной стоимости обедов и дней использования купонов."""
    if n == 0:
        return 0, 0, []

    INF = float("inf")

    # dp[i][j] - массив (n+1) строк на (n+2) столбцов.
    # n+2 чтобы безопасно обращаться к j+1, даже если j = n
    dp = [[INF] * (n + 2) for _ in range(n + 1)]
    dp[0][0] = 0  # В 0-й день с 0 купонов мы потратили 0 рублей

    # 1. Прямой проход (заполняем таблицу)
    for i in range(1, n + 1):
        p = prices[i - 1]
        for j in range(n + 1):
            # Вариант А: Покупаем за деньги
            cost_buy = INF
            if p > 500:
                # Получаем купон (вчера было j-1)
                if j > 0:
                    cost_buy = dp[i - 1][j - 1] + p
            else:
                # Не получаем купон (вчера было j)
                cost_buy = dp[i - 1][j] + p

            # Вариант Б: Используем купон (вчера было j+1)
            cost_use = dp[i - 1][j + 1]

            # Выбираем самый выгодный вариант
            dp[i][j] = min(cost_buy, cost_use)

    # 2. Ищем минимальную стоимость в последний день
    min_cost = INF
    best_j = 0
    for j in range(n + 1):
        # Если стоимости равны, лучше выбрать тот вариант,
        # где на руках осталось больше купонов (j)
        if dp[n][j] <= min_cost:
            if dp[n][j] < min_cost:
                min_cost = dp[n][j]
                best_j = j
            elif dp[n][j] == min_cost:
                best_j = max(best_j, j)

    # 3. Обратный проход (восстановление пути)
    curr_i = n
    curr_j = best_j
    used_days = []

    while curr_i > 0:
        p = prices[curr_i - 1]

        # Проверяем, могли ли мы в этот день использовать купон
        if curr_j + 1 <= n and dp[curr_i][curr_j] == dp[curr_i - 1][curr_j + 1]:
            used_days.append(curr_i)
            curr_j += 1
        else:
            # Значит покупали за деньги
            if p > 500:
                curr_j -= 1

        curr_i -= 1

    # Мы шли с конца, поэтому разворачиваем список дней
    used_days.reverse()

    return min_cost, len(used_days), used_days


if __name__ == "__main__":
    n, prices = get_input()

    if n > 0:
        total_cost, used_count, days = solve_restaurant(n, prices)

        # Вывод: Стоимость и количество потраченных купонов
        print(f"{total_cost} {used_count}")

        # Вывод: Номера дней через пробел (если были использованы)
        if days:
            print(" ".join(map(str, days)))
        else:
            print()  # Пустая строка, если купоны не тратились
