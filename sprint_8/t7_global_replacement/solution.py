def prefix_function(s: str) -> list[int]:
    """Вычисляет массив префиксной функции."""
    n = len(s)
    prefix = [0] * n
    for i in range(1, n):
        k = prefix[i - 1]
        while k > 0 and s[k] != s[i]:
            k = prefix[k - 1]
        if s[k] == s[i]:
            k += 1
        prefix[i] = k
    return prefix


def max_repetition_value(s: str) -> int:
    """Находит x — длину наибольшего повтора."""
    n = len(s)
    if n == 0:
        return 0

    prefix = prefix_function(s)

    # Последнее значение префиксной функции
    last_prefix_value = prefix[n - 1]

    # Длина минимального периода
    k = n - last_prefix_value

    # Если строка идеально делится на период, значит x = n / k
    if n % k == 0:
        return n // k
    else:
        # В противном случае строка является повтором только самой себя
        return 1


def get_input() -> str:
    """Считывает исходную строку."""
    return input().strip()


if __name__ == "__main__":
    s = get_input()
    print(max_repetition_value(s))
