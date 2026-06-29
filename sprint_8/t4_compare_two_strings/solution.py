def get_input() -> tuple[str, str]:
    """Считывает две строки из стандартного ввода."""
    a = input().strip()
    b = input().strip()
    return a, b


def compare_strings(a: str, b: str) -> int:
    """
    Фильтрует строки по четности позиции букв в алфавите
    и сравнивает их лексикографически.
    """
    # Используем list comprehension и трюк с ASCII-кодами.
    # Это работает быстрее, чем конкатенация строк в цикле.
    filtered_a = [char for char in a if ord(char) % 2 == 0]
    filtered_b = [char for char in b if ord(char) % 2 == 0]

    # Стандартное лексикографическое сравнение списков в Python
    if filtered_a < filtered_b:
        return -1
    elif filtered_a > filtered_b:
        return 1
    else:
        return 0


if __name__ == "__main__":
    str_a, str_b = get_input()
    print(compare_strings(str_a, str_b))
