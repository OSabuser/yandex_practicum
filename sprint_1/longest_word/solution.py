def get_assignments():
    text_length = int(input())

    if not 1 <= text_length <= 100000:
        return

    # Обрезали пробелы
    text = input().rstrip("\n")

    if len(text) != text_length:
        return

    return list(map(str, text.split()))


def get_max_longest_word(words):
    max_index = 0
    max_length = len(words[max_index])
    for index, word in enumerate(words):
        if len(word) > max_length:
            max_length = len(word)
            max_index = index

    return max_index, max_length


if __name__ == "__main__":
    assignments = get_assignments()
    if assignments is not None:
        max_index, max_length = get_max_longest_word(assignments)
        print(assignments[max_index])
        print(max_length)
