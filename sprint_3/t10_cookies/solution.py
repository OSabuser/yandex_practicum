def get_task_data():
    total_children = int(input())
    greeds_rate = list(map(int, input().split()))
    total_cookies = int(input())
    cookies_size = list(map(int, input().split()))
    return total_children, greeds_rate, total_cookies, cookies_size


def get_number_of_satisfied_children(greeds_rate, cookies_size):
    greeds_rate.sort()
    cookies_size.sort()

    child_ptr = 0
    cookie_ptr = 0

    # Проход по спискам
    while child_ptr < len(greeds_rate) and cookie_ptr < len(cookies_size):
        if greeds_rate[child_ptr] <= cookies_size[cookie_ptr]:
            child_ptr += 1
        cookie_ptr += 1

    return child_ptr


if __name__ == "__main__":
    n, g, m, c = get_task_data()
    print(get_number_of_satisfied_children(g, c))
