def get_input() -> tuple[int, list[int], int, list[int]]:
    """Считывает данные измерений и искомый шаблон."""
    n = int(input().strip())
    X = list(map(int, input().split()))
    m = int(input().strip())
    A = list(map(int, input().split()))
    return n, X, m, A


def shifted_search(n: int, X: list[int], m: int, A: list[int]) -> str:
    """
    Поиск шаблона со сдвигом через массивы разностей.
    Использует быстрое сравнение срезов списков.
    """
    # Крайний случай: шаблон из 1 элемента встречается везде
    if m == 1:
        return " ".join(map(str, range(1, n + 1)))

    # 1. Строим массивы разностей (перепады температур)
    # Длина dX будет n - 1, длина dA будет m - 1
    dX = [X[i] - X[i - 1] for i in range(1, n)]
    dA = [A[i] - A[i - 1] for i in range(1, m)]

    result = []
    pattern_len = m - 1

    # 2. Ищем точные совпадения с помощью быстрых срезов
    # Проходим до той позиции, где шаблон еще физически помещается
    for i in range(n - m + 1):
        # Взятие среза и оператор == в Python работают на уровне C
        if dX[i : i + pattern_len] == dA:
            # +1 так как по условию нумерация позиций начинается с единицы
            result.append(i + 1)

    return " ".join(map(str, result))


if __name__ == "__main__":
    n, X, m, A = get_input()
    print(shifted_search(n, X, m, A))
