def get_input_data():
    init_form_length = int(input())
    init_form_list = list(map(int, input().split()))
    add_number = input()

    return init_form_length, init_form_list, [int(digit) for digit in add_number]


def get_sum(len_1: int, n1: list[int], n2: int):
    """Вычисление суммы двух десятичных чисел, представленных в списочной форме"""
    result = []

    # Указатели на биты двух чисел. Начинаем с старших
    dec_ptr_1 = len_1 - 1
    dec_ptr_2 = len(n2) - 1

    carry_value = 0

    while dec_ptr_1 >= 0 or dec_ptr_2 >= 0 or carry_value:
        # Берем значение десятичного значения разряда, или дополняем нулем
        digit_val_1 = n1[dec_ptr_1] if dec_ptr_1 >= 0 else 0
        digit_val_2 = n2[dec_ptr_2] if dec_ptr_2 >= 0 else 0

        digit_sum = digit_val_1 + digit_val_2 + carry_value
        carry_value = digit_sum // 10  # Перенос, если digit_sum больше 9
        digit_sum = digit_sum % 10  # Остаток от суммы

        result.append(digit_sum)

        dec_ptr_1 -= 1
        dec_ptr_2 -= 1

    return result[::-1]


if __name__ == "__main__":
    init_form_length, init_form_list, add_number = get_input_data()
    print(*get_sum(init_form_length, init_form_list, add_number))
