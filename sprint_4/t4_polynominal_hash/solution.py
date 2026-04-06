def get_hash_data():
    a = int(input())
    m = int(input())
    string = input().strip()
    return a, m, string


def calculate_hash(a, m, string):
    """Реализация метода Горнера"""
    h = 0
    for c in string:
        h = (h * a + ord(c)) % m
    return h


if __name__ == "__main__":
    a, m, string = get_hash_data()
    print(calculate_hash(a, m, string))
