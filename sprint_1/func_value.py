def get_input_values():
    return map(int, input().split())


def get_func_value(a, x, b, c):
    return int(a * x * x + b * x + c)


if __name__ == "__main__":
    a, b, c, x = get_input_values()
    print(get_func_value(a, x, b, c))
