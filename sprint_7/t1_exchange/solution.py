def get_input() -> list[int]:
    """Считывает входные данные: количество дней и массив цен."""
    _n = int(input())

    prices = list(map(int, input().split()))
    return prices


def calculate_max_profit(prices: list[int]) -> int:
    """
    Жадный алгоритм: суммируем все положительные дельты
    между ценами завтрашнего и сегодняшнего дня.
    """
    if len(prices) < 2:
        return 0

    max_profit = 0
    # Проходим по массиву и собираем всю разницу на восходящих трендах
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit


if __name__ == "__main__":
    # Читаем данные
    prices = get_input()

    # Считаем и выводим результат
    result = calculate_max_profit(prices)
    print(result)
