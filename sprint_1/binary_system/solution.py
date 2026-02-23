def get_numbers():
    number_1 = input().rstrip("\n")
    number_2 = input().rstrip("\n")

    if not 0 < len(number_1) <= 10000:
        return

    if not 0 < len(number_2) <= 10000:
        return

    return (number_1, number_2)


def get_sum(number_1, number_2):
    result = []

    # Указатели на биты двух чисел. Начинаем с старших
    bit_ptr_1 = len(number_1) - 1
    bit_ptr_2 = len(number_2) - 1

    # Бит переноса. Равен 1, если сумма двух битов больше 1
    carry_bit = 0

    while bit_ptr_1 >= 0 or bit_ptr_2 >= 0 or carry_bit:
        # Берем текущее значение бита, если число "закончилось" дополняем нулями
        bit_value_1 = int(number_1[bit_ptr_1]) if bit_ptr_1 >= 0 else 0
        bit_value_2 = int(number_2[bit_ptr_2]) if bit_ptr_2 >= 0 else 0

        bit_sum = bit_value_1 + bit_value_2 + carry_bit

        carry_bit = bit_sum // 2  # Перенос, если bit_sum больше 1
        bit_sum = bit_sum % 2

        result.append(str(bit_sum))

        # Смещаем указатели
        bit_ptr_1 -= 1
        bit_ptr_2 -= 1

    return "".join(result[::-1])


if __name__ == "__main__":
    numbers = get_numbers()

    if numbers is not None:
        print(get_sum(*numbers))
