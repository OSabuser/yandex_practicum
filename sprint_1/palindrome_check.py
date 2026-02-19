def get_word():
    word = input().rstrip("\n")

    if not 0 < len(word) <= 20000:
        return
    return word.lower()


if __name__ == "__main__":
    word = get_word()
    if word is not None:
        reversed_word = word[::-1]
        for char in word:
            if char.isalnum():
                print("YES")
                break
        else:
            print("NO")
