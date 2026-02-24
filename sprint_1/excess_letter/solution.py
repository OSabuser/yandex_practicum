def get_strings():
    string_1 = input().strip()
    string_2 = input().strip()
    return string_1, string_2


# Известно, что s_2 длиннее чем s_1
def get_diff_char(s1, s2):
    code_sum_1 = 0
    code_sum_2 = 0

    for index in range(0, len(s2)):
        code_sum_1 += ord(s1[index]) if index < len(s1) else 0
        code_sum_2 += ord(s2[index])

    return chr(code_sum_2 - code_sum_1)


if __name__ == "__main__":
    print(get_diff_char(*get_strings()))
