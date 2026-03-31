def get_occupations():
    n = int(input())
    occupations = {}
    for _ in range(n):
        occupation = input()
        if occupations.get(occupation) is None:
            occupations[occupation] = 1
    return occupations


if __name__ == "__main__":
    occupations = get_occupations()

    for key in occupations.keys():
        print(f"{key}")
