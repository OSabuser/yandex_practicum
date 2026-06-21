def get_input() -> int:
    """Считывает порядковый номер числа Фибоначчи."""
    return int(input().strip())


def solve_fibonacci(n: int) -> int:
    """
    Вычисляет n-ое число Фибоначчи по модулю 10^9 + 7.
    Использует O(1) памяти.
    """
    MOD = 10**9 + 7

    # Базовые случаи
    if n == 0 or n == 1:
        return 1

    prev2 = 1  # F_0
    prev1 = 1  # F_1
    # Итеративно вычисляем от 2 до n
    for _ in range(2, n + 1):
        # Берем остаток на каждом шаге сложения
        curr = (prev1 + prev2) % MOD
        prev2 = prev1
        prev1 = curr

    return prev1


if __name__ == "__main__":
    n = get_input()
    print(solve_fibonacci(n))
