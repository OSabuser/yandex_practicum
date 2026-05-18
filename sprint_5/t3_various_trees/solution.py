def get_max_number():
    return int(input())


# Количество различных BST с уникальными числами от 1 до n — это n-е число Каталана C_n.
# C_n = [(2n)!] / [n! (n + 1)!]
# Альтернативный вариант через формулу
def count_bst_formula(n):
    """Прямой расчёт через формулу Каталана."""
    if n <= 1:
        return 1

    from math import factorial

    return factorial(2 * n) // (factorial(n + 1) * factorial(n))


if __name__ == "__main__":
    max_number = get_max_number()
    print(count_bst_formula(max_number))
