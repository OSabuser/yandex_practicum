def get_pressed_keys():
    return input()


def show_combinations(pressed_keys):
    keys_dict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def get_combinations(index, prefix):
        if index == len(pressed_keys):
            results.append(prefix)
            return
        for letter in keys_dict[pressed_keys[index]]:
            get_combinations(index + 1, prefix + letter)

    results = []
    get_combinations(0, "")
    return results

    get_combinations("")


if __name__ == "__main__":
    keys = get_pressed_keys()
    print(*show_combinations(keys))
