# ССЫЛКА НА ОТЧЁТ: https://contest.yandex.ru/contest/22781/run-report/158838557/
#
# 1. Принцип работы Deque
# > Дека построена на кольцевом буфере. Операции извлечения и добавления элементов
# из/в начало/конец деки работают с использованием указателей `head`,`tail`. `push_back`,
# `pop_front` работают также, как и в обычной очереди на кольцевом буфере: при
# добавлении элемента в конец очереди `tail` увеличивается на единицу, при извлечении
# элемента из начала - двигаем указатель `head` на единицу вперед. `push_front`,`pop_back`
# работают аналогично, но в обратную сторону: при добавлении элемента в начало очереди
# перемещается  `head` на единицу назад, при извлечении элемента из конца очереди -
# двигаем назад `tail`.
#
# 2. Доказательство корректности
# > Для этого достаточно рассмотреть несколько ситуаций:
# > 1) Если очередь пуста, то `head` и `tail` равны.
# > 2) При `push_back` c `tail`= queue_size - 1,`tail` сместится на начальную позицию в массиве
# (первый элемент).
# > 3) При `push_front` c `head` = 0,`head` сместится на конечную позицию в массиве `queue_size - 1`
# > 4) Аналогично, для `pop_front` и `pop_back`:
# - при pop_front c `head`= queue_size - 1 `head` сместится начальную позицию в массиве
# - при pop_back c `tail`= 0 `tail` сместится начальную позицию в массиве
#  Всё это сводится к тому, чтобы осуществлять корректные циклические смещения указателей:
#
#  Для `push_back` сразу после записи:
#  self._tail = (self._tail + 1) % self._max_length
#  Для `pop_front` сразу после чтения:
#  self._head = (self._head + 1) % self._max_length
#  Для `pop_back` перед чтения:
#  self._tail = (self._tail - 1 + self._max_length) % self._max_length
#  Для `push_front` перед записью:
#  self._head = (self._head - 1 + self._max_length) % self._max_length
#
# Цикличность здесь обеспечивается операцией % self._max_length
#
# 3. Временная сложность
# > Все типы операций `push`,`pop` выполняются за O(1). Каждая из этих операций представляет
# собой: смещение указателя head/tail вправо/влево, изменение текущего размера очереди и
# чтение/запись в массив по индексу без переаллокаций (размер массива жёстко зафиксирован).
#
# 4. Пространственная сложность
# > Дека потребует O(N) памяти(N - размер очереди, определяется пользователем) + немного накладных
# расходов для хранения указателей и вспомогательных переменных предсказуемо O(1) =>
# O(N) - общее потребление.
#
class MyDequeueSized:
    def __init__(self, queue_size):
        self._queue = [None] * queue_size
        self._head = 0
        self._tail = 0
        self._max_length = queue_size
        self._queue_size = 0

    def push_back(self, item):
        """Добавление элемента ${item} в конец очереди"""
        if self._queue_size == self._max_length:
            raise ValueError("Очередь переполнена!")

        # Добавляем элемент в конец очереди
        self._queue[self._tail] = item
        # Смещаем указатель на следующую позицию
        self._tail = (self._tail + 1) % self._max_length
        self._queue_size += 1
        return item

    def push_front(self, item):
        """Добавление элемента ${item} в начало очереди"""
        if self._queue_size == self._max_length:
            raise ValueError("Очередь переполнена!")

        # Смещаем сначала указатель head на следующую позицию слева
        # Старый элемент на который указывал head, не трогаем
        self._head = (self._head - 1 + self._max_length) % self._max_length
        self._queue[self._head] = item
        self._queue_size += 1
        return item

    def pop_back(self):
        """Убрать элемент из конца очереди и вернуть его вызывающей стороне"""
        if self._queue_size == 0:
            raise ValueError("Пустая очередь!")

        # Смещаем сначала указатель tail на следующую позицию слева
        # При следующих вставках front, будем использовать его
        # а пока, достанем отсюда значение
        self._tail = (self._tail - 1 + self._max_length) % self._max_length
        element = self._queue[self._tail]
        self._queue[self._tail] = None
        self._queue_size -= 1
        return element

    def pop_front(self):
        """Убрать элемент из начала очереди и вернуть его вызывающей стороне"""
        if self._queue_size == 0:
            raise ValueError("Пустая очередь!")

        element = self._queue[self._head]
        self._queue[self._head] = None
        self._head = (self._head + 1) % self._max_length
        self._queue_size -= 1
        return element

    def get_queue_size(self):
        """Возвращение размера очереди"""
        return self._queue_size

    def run_user_command(self, command: str):
        """Выполнение пользовательской командой над Deque-очередью"""
        # Сделал тут простенько
        # Так-то можно было держать массив указателей на функции/лямбды
        # Если command_output = None, вызывающая сторона ничего
        # печатать не будет
        command_output = None
        command, *args = command.split()
        match command:
            case "push_front":
                try:
                    self.push_front(int(args[0]))
                except ValueError:
                    command_output = "error"
            case "push_back":
                try:
                    self.push_back(int(args[0]))
                except ValueError:
                    command_output = "error"
            case "pop_front":
                try:
                    command_output = self.pop_front()
                except ValueError:
                    command_output = "error"

            case "pop_back":
                try:
                    command_output = self.pop_back()
                except ValueError:
                    command_output = "error"

        return command_output


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
    queue = MyDequeueSized(queue_size)

    for command in user_commands:
        result = queue.run_user_command(command)
        if result is not None:
            print(result)
