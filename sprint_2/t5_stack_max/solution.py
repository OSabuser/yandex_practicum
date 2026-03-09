class Stack:
    def __init__(self):
        self.__current_max = 0
        self.__stack_size = 0
        self.__items = []

    def push(self, item):
        # Инициализация значения максимального элемента в списке
        if self.__stack_size == 0:
            self.__current_max = item
        else:
            # Обновление значения максимального элемента в списке
            if item > self.__items[self.__stack_size - 1][1]:
                self.__current_max = item

        self.__stack_size += 1
        self.__items.append((item, self.__current_max))

    def pop(self):
        if self.__stack_size > 0:
            self.__stack_size -= 1
            stack_element = self.__items.pop()
            self.__current_max = self.get_max()
            return stack_element[0]
        return "error"

    def get_max(self):
        if self.__stack_size > 0:
            return self.__items[self.__stack_size - 1][1]
        return "None"

    def run_user_command(self, command: str):
        try:
            arg1, arg2 = command.split()
        except ValueError:
            arg1 = command
            if arg1 == "pop":
                if self.pop() == "error":
                    print("error")
            elif arg1 == "get_max":
                print(self.get_max())
        else:
            if arg1 == "push":
                self.push(int(arg2))


def get_user_commands():
    number_of_commands = int(input())
    commands = []

    for _ in range(number_of_commands):
        commands.append(input())
    return commands


if __name__ == "__main__":
    user_commands = get_user_commands()
    stack = Stack()
    for command in user_commands:
        stack.run_user_command(command)
