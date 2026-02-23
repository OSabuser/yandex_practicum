def get_word():
    word = input().rstrip("\n")

    if not 0 < len(word) <= 20000:
        return
    return word.lower()


def is_word_palindrome(text: str):
    text_length = len(text)

    # Если слово состоит из одного символа, то оно не является палиндромом
    if text_length == 1:
        return False

    # Инициализируем указатели на первый и последний символ строки
    left_symbol_ptr = 0
    right_symbol_ptr = text_length - 1

    while left_symbol_ptr < right_symbol_ptr:
        # Пропускаем все кроме цифр и букв
        if not text[left_symbol_ptr].isalnum():
            left_symbol_ptr += 1
            continue
        # Пропускаем все кроме цифр и букв
        if not text[right_symbol_ptr].isalnum():
            right_symbol_ptr -= 1
            continue

        print("To compare:", text[left_symbol_ptr], text[right_symbol_ptr])
        # Сюда попадаем, тогда, когда оба указателя указывают на валидный символ
        if text[left_symbol_ptr] != text[right_symbol_ptr]:
            return False

        # Перемещаем указатели на следующий символ
        left_symbol_ptr += 1
        right_symbol_ptr -= 1

    return True


if __name__ == "__main__":
    word = get_word()

    if word is not None:
        if is_word_palindrome(word):
            print("TRUE")
        else:
            print("FALSE")
