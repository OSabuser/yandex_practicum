def get_input() -> tuple[int, int, list[str]]:
    """Считывает размеры и карту цветочного поля."""
    n, m = map(int, input().split())
    # Считываем поле построчно
    grid = [input().strip() for _ in range(n)]
    return n, m, grid


def solve_flower_field(n: int, m: int, grid: list[str]) -> int:
    """ДП с оптимизацией памяти для поиска максимума цветов."""

    # Cтарт в левом верхнем углу (0, 0), финиш в правом нижнем (n-1, m-1).
    # Двигаемся строго ВНИЗ и ВПРАВО.
    grid.reverse()

    # Храним только одну "предыдущую" строку для расчета текущей
    dp = [0] * (m + 1)

    for i in range(n):
        # Массив для расчета текущей строки
        curr_dp = [0] * (m + 1)

        for j in range(1, m + 1):
            # Переводим символ '0' или '1' в число.
            # Индекс j-1, так как в dp мы добавили фиктивный 0-й столбец (паддинг)
            flower = int(grid[i][j - 1])

            # Максимум из: шага сверху (dp[j]) или шага слева (curr_dp[j-1])
            curr_dp[j] = max(dp[j], curr_dp[j - 1]) + flower

        # Текущая строка становится "предыдущей" для следующей итерации
        dp = curr_dp

    # Ответ всегда будет лежать в последней ячейке последней посчитанной строки
    return dp[m]


if __name__ == "__main__":
    n, m, field = get_input()
    print(solve_flower_field(n, m, field))
