class LinkedNode:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class MyLinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.queue_size = 0

    def put(self, value):
        """Добавление элемента ${item} в очередь"""
        new_node = LinkedNode(value)
        if self.head is None:
            # Инициализация указателей
            self.head = new_node
            self.tail = new_node
        else:
            # Предыдущий элемент указывает на новый элемент
            self.tail.next_item = new_node
            # Обновление указателя добавления элемента (конец очереди)
            self.tail = new_node
        self.queue_size += 1

    def get(self):
        """Убрать ноду из начала очереди и вернуть ее значение вызывающей стороне"""
        if self.head is None:
            # Очередь пуста
            return None
        element = self.head.value
        # Голова теперь указывает на следующий элемент после удалённого(головы)
        self.head = self.head.next_item
        self.queue_size -= 1
        return element

    def size(self):
        """Возвращение размера очереди"""
        return self.queue_size

    def run_user_command(self, command: str):
        try:
            arg1, arg2 = command.split()
        except ValueError:
            # Команда не содержит аргументов
            arg1 = command
            if arg1 == "get":
                result = self.get()
                if result is None:
                    return "error"
                return result
            elif arg1 == "size":
                return self.size()
        else:
            # Команда содержит аргумент
            if arg1 == "put":
                return self.put(int(arg2))


def get_user_commands():
    """Получение набора пользовательских команд"""
    number_of_commands = int(input())

    commands = []
    for _ in range(number_of_commands):
        commands.append(input())
    return commands


if __name__ == "__main__":
    user_commands = get_user_commands()
    linked_queue = MyLinkedQueue()
    for command in user_commands:
        result = linked_queue.run_user_command(command)
        if result is not None:
            print(result)
