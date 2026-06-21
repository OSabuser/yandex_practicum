def get_input() -> list[tuple[float, float, str, str]]:
    """Считывает данные, возвращая float-значения для логики и исходные строки для вывода."""
    try:
        n = int(input().strip())
    except EOFError:
        return []

    lessons = []
    for _ in range(n):
        s_str, e_str = input().split()
        # Сохраняем: (float_start, float_end, orig_start, orig_end)
        lessons.append((float(s_str), float(e_str), s_str, e_str))

    return lessons


def solve_schedule(lessons: list[tuple[float, float, str, str]]) -> list[tuple[str, str]]:
    """
    Жадный алгоритм. Сортируем по времени конца, а затем по времени начала.
    """
    if not lessons:
        return []

    # Сортировка: сначала по x[1] (end), затем по x[0] (start)
    lessons.sort(key=lambda x: (x[1], x[0]))

    result = []
    last_end = -1.0 # Время начала/конца всегда >= 0

    for start_f, end_f, start_str, end_str in lessons:
        # Если урок начинается не раньше, чем закончился предыдущий - берем его
        if start_f >= last_end:
            result.append((start_str, end_str))
            last_end = end_f
    return result


if __name__ == "__main__":
    lessons = get_input()

    if lessons:
        schedule = solve_schedule(lessons)
        print(len(schedule))
        for start_str, end_str in schedule:
            print(f"{start_str} {end_str}")
    else:
        print(0)
