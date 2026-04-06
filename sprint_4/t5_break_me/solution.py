import itertools
import string

ALPHABET = string.ascii_lowercase


def calculate_hash(a, m, hashed_string):
    """Реализация метода Горнера"""
    h = 0
    for c in hashed_string:
        h = (h * a + ord(c)) % m
    return h


def all_strings(max_len: int, alphabet=ALPHABET):
    for length in range(1, max_len + 1):
        for tup in itertools.product(alphabet, repeat=length):
            yield "".join(tup)


def find_collision(a: int, m: int, max_len: int = 5):
    seen = {}  # hash -> string

    for s in all_strings(max_len):
        h = calculate_hash(a, m, s)
        if h in seen and seen[h] != s:
            return h, seen[h], s  # коллизия найдена
        seen[h] = s

    return None  # в выбранном пространстве нет коллизии


if __name__ == "__main__":
    a = 1000
    m = 123987123

    h, s1, s2 = find_collision(a=a, m=m, max_len=1000)
    print(h, s1, s2)
    print(f"Hash 1: {calculate_hash(a=a, m=m, hashed_string=s1)}")
    print(f"Hash 2: {calculate_hash(a=a, m=m, hashed_string=s2)}")
