# Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и на экране появляются
# три случайных числа. Если все три числа оказываются одной чётности, игрок выигрывает.
# Напишите программу, которая по трём числам определяет, выиграл игрок или нет.
def get_input_values():
    return list(map(int, input().split()))


def make_decision(inspected_list):
    if len(inspected_list) != 3:
        return "ERROR"

    for value in inspected_list:
        if abs(value) > 10**9:
            return "ERROR"

    return (
        "WIN"
        if all(n % 2 == 0 for n in inspected_list) or all(n % 2 != 0 for n in inspected_list)
        else "FAIL"
    )


if __name__ == "__main__":
    values = get_input_values()
    print(make_decision(values))
