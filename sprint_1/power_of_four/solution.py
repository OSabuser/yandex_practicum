def get_number() -> int:
    number = int(input())

    if not 0 < number <= 10000:
        return -1
    return number


def is_number_a_power_of_four(number: int) -> str:
    while number % 4 == 0:
        number = number // 4

    return "True" if number == 1 else "False"


if __name__ == "__main__":
    number = get_number()

    if number != -1:
        print(is_number_a_power_of_four(number))
