def get_strings():
    string_1 = input().strip()
    string_2 = input().strip()
    return string_1, string_2


_LATIN_LETTERS = 26


def compare_strings(string_1, string_2):
    if len(string_1) != len(string_2):
        return "NO"

    # Символы из string_1 [индекс i] пееходящие в string_2 [индекс j]
    # -1 - соответствие не найдено
    mapST = [-1] * _LATIN_LETTERS

    # Символы из string_2 [индекс j] пееходящие в string_1 [индекс i]
    # -1 - соответствие не найдено
    mapTS = [-1] * _LATIN_LETTERS

    for char_1, char_2 in zip(string_1, string_2, strict=True):
        # Переводим символы в числовые индексы, начиная с нуля (a = 0, b = 1, ..., z = 25)
        i = ord(char_1) - ord("a")
        j = ord(char_2) - ord("a")

        if mapST[i] == -1 and mapTS[j] == -1:
            # Оба символа еще не встречались (ставим соответствие)
            mapST[i] = j
            mapTS[j] = i
        elif mapST[i] != j or mapTS[j] != i:
            # Символы не совпадают
            return "NO"
    return "YES"


if __name__ == "__main__":
    s, t = get_strings()

    print(compare_strings(s, t))
