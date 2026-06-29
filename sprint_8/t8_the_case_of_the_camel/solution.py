def get_skeletons(n: int) -> list[tuple[str, str]]:
    """Создает список кортежей (скелет_заглавных, полное_имя)."""
    data = []
    for _ in range(n):
        name = input().strip()
        # Извлекаем только заглавные буквы
        skeleton = "".join([c for c in name if c.isupper()])
        data.append((skeleton, name))
    return data


def get_results():
    # Читаем количество названий
    line = input()
    if not line:
        return
    n = int(line.strip())

    # Препроцессинг базы
    names_data = get_skeletons(n)

    # Читаем количество запросов
    line = input()
    if not line:
        return
    m = int(line.strip())

    for _ in range(m):
        pattern = input().strip()

        # Находим все строки, скелет которых начинается с паттерна
        matches = [name for skeleton, name in names_data if skeleton.startswith(pattern)]

        # Сортируем и выводим согласно требованиям
        if matches:
            matches.sort()
            print("\n".join(matches))
        else:
            print("")


if __name__ == "__main__":
    get_results()
