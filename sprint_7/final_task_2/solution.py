def get_input() -> tuple[int, list[int]]:
    """Считывает количество партий и массив заработанных очков."""
    n_str = input().strip()
    if not n_str:
        return 0, []

    n = int(n_str)

    # Обработка крайнего случая: n = 0
    if n == 0:
        return 0, []

    points = list(map(int, input().split()))
    return n, points


def can_partition(n: int, points: list[int]) -> bool:
    """
    Проверяет, можно ли разбить массив на две части с равной суммой,
    используя динамическое программирование (задача о рюкзаке).
    """
    total_sum = sum(points)

    # Если общая сумма нечетная, поделить поровну нельзя
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    # dp[i] означает: можно ли набрать сумму i из доступных очков
    dp = [False] * (target + 1)
    dp[0] = True  # Сумму 0 можно собрать всегда (пустое подмножество)

    # Проходим по очкам за каждую выигранную партию
    for point in points:
        # Идем с конца (от target до point), чтобы использовать
        # каждое число из points строго один раз!
        for i in range(target, point - 1, -1):
            # Если мы уже могли собрать сумму i, она остается True.
            # Либо, если мы могли собрать сумму (i - point), то добавив
            # текущий point, мы сможем собрать сумму i.
            dp[i] = dp[i] or dp[i - point]

    return dp[target]


if __name__ == "__main__":
    n, match_points = get_input()
    print(can_partition(n, match_points))
