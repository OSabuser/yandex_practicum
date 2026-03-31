def get_round_results():
    n = int(input())
    results = input().split()
    return n, results


def get_max_draw_length(results):
    pref = 0

    first = {0: 0}  # сумма -> первая позиция (префикс до неё)
    best_len = 0

    for i, ch in enumerate(results, start=1):
        pref += -1 if ch == "0" else 1

        if pref in first:
            best_len = max(best_len, i - first[pref])
        else:
            first[pref] = i

    return best_len


if __name__ == "__main__":
    n, results = get_round_results()

    print(get_max_draw_length(results))
