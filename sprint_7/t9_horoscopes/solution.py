def get_input() -> tuple[int, list[int], int, list[int]]:
    """Считывает длины и сами последовательности."""
    n = int(input().strip())
    A = list(map(int, input().split()))
    m = int(input().strip())
    B = list(map(int, input().split()))
    return n, A, m, B


def solve_lcs(n: int, A: list[int], m: int, B: list[int]) -> tuple[int, list[int], list[int]]:
    """
    Находит длину НОП и восстанавливает индексы.
    """
    # 1. Прямой проход: заполняем таблицу динамики
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 2. Обратный проход: восстанавливаем ответ
    lcs_length = dp[n][m]

    # Если НОП нет, сразу возвращаем пустые списки
    if lcs_length == 0:
        return 0, [], []

    indices_A = []
    indices_B = []

    i, j = n, m
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            # Элементы совпали — добавляем их индексы.
            # Сохраняем 1-based индексы (так как i и j у нас и так от 1)
            indices_A.append(i)
            indices_B.append(j)
            # Шагаем по диагонали
            i -= 1
            j -= 1
        elif dp[i - 1][j] == dp[i][j]:
            # Максимум пришел сверху
            i -= 1
        else:
            # Максимум пришел слева
            j -= 1

    # Разворачиваем списки, так как мы шли с конца
    indices_A.reverse()
    indices_B.reverse()

    return lcs_length, indices_A, indices_B


if __name__ == "__main__":
    n, seq_A, m, seq_B = get_input()

    length, idx_A, idx_B = solve_lcs(n, seq_A, m, seq_B)

    print(length)
    if length > 0:
        # Выводим индексы через пробел
        print(" ".join(map(str, idx_A)))
        print(" ".join(map(str, idx_B)))
