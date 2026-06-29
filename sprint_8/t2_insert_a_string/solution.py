def get_input() -> tuple[str, int, list[tuple[str, int]]]:
    """Считывает исходную строку и данные для вставки."""
    s = input().strip()

    # Обрабатываем случай пустой строки, если вдруг попадутся кривые тесты
    if not s:
        return "", 0, []

    n = int(input().strip())

    insertions_data = []
    for _ in range(n):
        # Читаем пару "строка индекс"
        t, k = input().split()
        insertions_data.append((t, int(k)))

    return s, n, insertions_data


def get_inserted_string(s: str, insertions_data: list[tuple[str, int]]) -> str:
    """
    Собирает новую строку за O(N) с помощью паттерна Builder (через список),
    избегая квадратичной сложности конкатенации неизменяемых строк.
    """
    # Инициализируем массив вставок пустыми строками.
    # Размер len(s) + 1, так как k может указывать на самый конец строки.
    insertions = [""] * (len(s) + 1)

    # Заполняем массив вставок по их индексам
    for t, k in insertions_data:
        insertions[k] = t

    # Динамический массив для сборки финальной строки
    result = []

    # Проходим по всем возможным позициям для вставки
    for i in range(len(s) + 1):
        # Если в этой позиции есть подаренная строка — добавляем её
        if insertions[i]:
            result.append(insertions[i])

        # Добавляем символ исходной строки (пока не вышли за её пределы)
        if i < len(s):
            result.append(s[i])

    # Собираем всё воедино за одну аллокацию памяти
    return "".join(result)


if __name__ == "__main__":
    original_str, count, insertions_list = get_input()

    if original_str:
        print(get_inserted_string(original_str, insertions_list))
