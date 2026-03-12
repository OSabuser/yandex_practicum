class MyQueueSized:
    def __init__(self, queue_size):
        self.queue = [None] * queue_size
        self.head = 0
        self.tail = 0
        self.max_length = queue_size
        self.queue_size = 0

    def push(self, item):
        """Добавление элемента ${item} в очередь"""
        if self.queue_size == self.max_length:
            # Очередь заполнена
            return None
        self.queue[self.tail] = item
        # Обновление указателя добавления элемента
        self.tail = (self.tail + 1) % self.max_length
        self.queue_size += 1
        return item

    def pop(self):
        """Убрать элемент из начала очереди и вернуть его вызывающей стороне"""
        if self.queue_size == 0:
            # Очередь пуста
            return None

        element = self.queue[self.head]
        self.queue[self.head] = None
        # Обновление указателя удаления элемента
        self.head = (self.head + 1) % self.max_length
        self.queue_size -= 1
        return element

    def peek(self):
        """Вывод первого элемента в очереди"""
        if self.queue_size == 0:
            # Очередь пуста
            return None
        return self.queue[self.head]

    def size(self):
        """Возвращение размера очереди"""
        return self.queue_size

    def run_user_command(self, command: str):
        try:
            arg1, arg2 = command.split()
        except ValueError:
            arg1 = command
            if arg1 == "pop":
                result = self.pop()
                if result is None:
                    return "None"
                return result
            elif arg1 == "peek":
                result = self.peek()
                if result is None:
                    return "None"
                return result
            elif arg1 == "size":
                return self.size()
        else:
            if arg1 == "push":
                result = self.push(int(arg2))
                if result is None:
                    return "error"
        return None


def get_user_commands():
    """Получение размера очереди и набора пользовательских команд"""
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
        result = queue.run_user_command(command)
        if result is not None:
            print(result)
