def get_input_data():
    s1 = input()
    s2 = input()
    return s1, s2


def is_subsequence(candidate, string):
    sub_ptr = 0
    str_ptr = 0
    while sub_ptr < len(candidate) and str_ptr < len(string):
        if candidate[sub_ptr] == string[str_ptr]:
            sub_ptr += 1
        str_ptr += 1
    # sub_ptr == len(candidate) <=> символы кандидата встречаются в строке
    return "True" if sub_ptr == len(candidate) else "False"


if __name__ == "__main__":
    s1, s2 = get_input_data()
    print(is_subsequence(s1, s2))
