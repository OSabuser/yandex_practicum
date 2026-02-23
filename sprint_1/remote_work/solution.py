def get_number() -> int:
    number = int(input())

    if not 0 <= number <= 10000:
        return -1
    return number


def get_str_bin_representation(number: int) -> str:
    if number == 0:
        return "0"

    bin_represenation = []
    result = number

    while result != 0:
        bin_represenation.append(str(result % 2))
        result = result // 2

    return "".join(bin_represenation[::-1])


if __name__ == "__main__":
    number = get_number()

    if number != -1:
        print(get_str_bin_representation(number))
