def get_input() -> str:
    """Считывает исходную строку."""
    return input().strip()


def get_reversed_string(s: str) -> str:
    """
    Алгоритмическое решение с помощью двух указателей.
    Идем с конца строки в начало.
    """
    result = []
    right = len(s) - 1

    while right >= 0:
        # Пропускаем пробелы
        if s[right] == " ":
            right -= 1
            continue

        # Как только нашли букву, ставим левый указатель сюда же
        left = right
        # Двигаем левый указатель, пока не упремся в пробел или начало строки
        while left >= 0 and s[left] != " ":
            left -= 1

        # Вырезаем слово и добавляем в результат
        result.append(s[left + 1 : right + 1])

        # Перепрыгиваем обработанное слово
        right = left

    return " ".join(result)


if __name__ == "__main__":
    text = get_input()
    print(get_reversed_string(text))
