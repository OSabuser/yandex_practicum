def get_input() -> tuple[str, str]:
    """Считывает имя из паспорта и имя из базы."""
    passport_name = input().strip()
    db_name = input().strip()
    return passport_name, db_name


def solve_border_control(s1: str, s2: str) -> str:
    """
    Проверяет, отличаются ли строки не более чем на 1 символ
    (расстояние Левенштейна <= 1) за линейное время O(N).
    """
    # Если разница длин больше 1, одной операцией не обойтись
    if abs(len(s1) - len(s2)) > 1:
        return "FAIL"

    # Для упрощения логики гарантируем, что s1 всегда короче или равна s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    i = 0
    j = 0
    edits_count = 0

    # Проходим по обеим строкам
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            # Символы совпали — двигаем оба указателя
            i += 1
            j += 1
        else:
            # Нашли отличие
            edits_count += 1
            if edits_count > 1:
                return "FAIL"

            # Если длины равны, это была замена (сдвигаем оба)
            if len(s1) == len(s2):
                i += 1
                j += 1
            # Если длины разные, это вставка/удаление (сдвигаем только длинный)
            else:
                j += 1

    # Крайний случай: если в конце более длинной строки остался 1 лишний символ,
    # а цикл while завершился (например "Коля" и "Коляя").
    # Это добавит ровно 1 отличие (при условии, что ранее отличий не было).
    if j < len(s2):
        edits_count += 1

    if edits_count <= 1:
        return "OK"
    else:
        return "FAIL"


if __name__ == "__main__":
    passport, db = get_input()
    print(solve_border_control(passport, db))
