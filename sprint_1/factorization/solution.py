def get_number() -> int:
    number = int(input())

    if not 1 < number <= 10**9:
        return -1
    return number


def factorize(number: int) -> list[int]:
    divisor = 2
    result = []
    while divisor**2 <= number:
        if number % divisor == 0:
            # Найден очередной множитель
            number //= divisor
            result.append(divisor)
        else:
            divisor += 1
    if number != 1:
        # Добавляем оставшееся просто число
        result.append(number)

    return result


if __name__ == "__main__":
    number = get_number()

    if number != -1:
        print(*factorize(number))
