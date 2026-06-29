def get_input() -> str:
    """Считывает исходную строку."""
    return input().strip()


def prefix_function(s):
    # Функция возвращает массив длины |s|
    n = len(s)
    prefix = [None] * n
    prefix[0] = 0
    for i in range(1, n):
        k = prefix[i - 1]
        while k > 0 and s[k] != s[i]:
            k = prefix[k - 1]
        if s[k] == s[i]:
            k += 1
        prefix[i] = k
    return prefix


if __name__ == "__main__":
    string = get_input()
    print(*prefix_function(string))
