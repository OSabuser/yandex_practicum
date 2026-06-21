def get_input() -> tuple[int, int, list[int]]:
    """Считывает целевую сумму, количество номиналов и сами номиналы."""
    m = int(input().strip())
    n = int(input().strip())
    coins = list(map(int, input().split()))
    return m, n, coins


def solve_atm_combinations(m: int, coins: list[int]) -> int:
    """
    ДП для подсчета количества уникальных комбинаций монет,
    дающих в сумме m.
    """
    # dp[i] - количество способов набрать сумму i
    dp = [0] * (m + 1)

    # Базовый случай: собрать сумму 0 можно ровно 1 способом
    dp[0] = 1

    # Внешний цикл по монетам гарантирует, что мы не будем считать
    # перестановки вроде (1+2) и (2+1) за разные способы.
    for coin in coins:
        # Внутренний цикл по суммам: пытаемся добавить текущую монету
        # ко всем возможным суммам, начиная с номинала самой монеты.
        for i in range(coin, m + 1):
            dp[i] += dp[i - coin]

    return dp[m]


if __name__ == "__main__":
    target_sum, _, banknotes = get_input()
    print(solve_atm_combinations(target_sum, banknotes))
