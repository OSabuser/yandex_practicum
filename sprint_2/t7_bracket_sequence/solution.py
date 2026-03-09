class Stack:
    def __init__(self):
        self.__stack_size = 0
        self.__items = []

    def push(self, item):
        self.__stack_size += 1
        self.__items.append(item)

    def pop(self):
        if self.__stack_size > 0:
            self.__stack_size -= 1
            return self.__items.pop()
        return "error"

    def top(self):
        if self.__stack_size > 0:
            return self.__items[self.__stack_size - 1]
        return "error"


def get_bracket_sequence():
    return input()


def is_correct_bracket_seq(sequence: str):
    # Пустая строка считается валидной скобочной последовательностью
    if len(sequence) == 0:
        return True

    # Количество скобок должно быть четным
    if len(sequence) % 2 != 0:
        return False

    stack = Stack()

    bracket_pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for bracket in sequence:
        if bracket in "([{":
            stack.push(bracket)
        elif bracket in ")]}":
            last_bracket = stack.top()
            if last_bracket == "error":
                return False
            # Проверка соответствия скобок
            if last_bracket != bracket_pairs[bracket]:
                return False
            # Убираем открывающую скобку, соответствующую текущей
            stack.pop()
    # В корректной скобочной последовательности количество открывающих и закрывающих
    # скобок одного типа должно быть равным, т.е. стек должен быть пуст
    return stack.top() == "error"


if __name__ == "__main__":
    sequence = get_bracket_sequence()
    if is_correct_bracket_seq(sequence):
        print("True")
    else:
        print("False")
