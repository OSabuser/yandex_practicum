def get_input() -> tuple[int, int, list[int]]:
    """Считывает целевую сумму, количество номиналов и сам массив номиналов."""
    x = int(input().strip())
    _k = int(input().strip())
    # Считываем номиналы. Сразу можно отсеять те, что больше x,
    # так как они нам точно не понадобятся.
    coins = list(map(int, input().split()))
    return x, _k, coins


def solve_atm(x: int, coins: list[int]) -> int:
    """Динамическое программирование для поиска минимального числа купюр."""
    # Очищаем от дубликатов для ускорения алгоритма
    unique_coins = set(coins)

    # Инициализируем массив DP бесконечностью
    dp = [float("inf")] * (x + 1)
    dp[0] = 0  # Для суммы 0 нужно 0 купюр

    # Проходим по каждому уникальному номиналу
    for coin in unique_coins:
        # Обновляем значения DP только для сумм, куда эта купюра влезает
        for i in range(coin, x + 1):
            # Если сумму i - coin можно собрать, пробуем собрать i
            if dp[i - coin] != float("inf"):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Если значение осталось бесконечностью, значит сумму собрать нельзя
    return dp[x] if dp[x] != float("inf") else -1


if __name__ == "__main__":
    target_sum, k, banknotes = get_input()
    print(solve_atm(target_sum, banknotes))
