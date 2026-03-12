class MyQueueSized:
    def __init__(self, queue_size):
        self.queue = [None] * queue_size
        self.head = 0
        self.tail = 0
        self.max_n = queue_size
        self.size = 0

    def push(self, item):
        """Добавление элемента ${item} в очередь"""
        pass

    def pop(self):
        """Убрать элемент из начала очереди и вернуть его вызывающей стороне"""
        pass

    def peek(self):
        """Вывод первого элемента в очереди"""
        pass

    def size(self):
        """Возвращение размера очереди"""
        return self.size

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
            elif arg1 == "top":
                print(self.top())
        else:
            if arg1 == "push":
                self.push(int(arg2))


def get_user_commands():
    number_of_commands = int(input())

    max_queue_size = int(input())

    commands = []
    for _ in range(number_of_commands):
        commands.append(input())
    return max_queue_size, commands


if __name__ == "__main__":
    queue_size, user_commands = get_user_commands()
    queue = MyQueueSized(queue_size)

    for command in user_commands:
        queue.run_user_command(command)
