def get_task_data():
    houses, budget = map(int, input().split())
    prices = list(map(int, input().split()))
    return houses, budget, prices


def get_number_of_houses_to_buy(houses, budget, prices):
    can_buy = 0
    prices.sort()
    for price in prices:
        if budget >= price:
            budget -= price
            can_buy += 1

    return can_buy


if __name__ == "__main__":
    houses, budget, prices = get_task_data()
    print(get_number_of_houses_to_buy(houses, budget, prices))
