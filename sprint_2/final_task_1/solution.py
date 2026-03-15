# ССЫЛКА НА ОТЧЁТ: https://contest.yandex.ru/contest/22781/run-report/158610375/
# > Основная идея:
# В целом, в задаче "Ограниченная очередь" мы уже реализовали обычную очередь на кольцевом буфере
# Бонусом из этой задачи мы получаем реализованные методы: push_back(val) & pop_front без
# модификаиций. Эти методы в общем-то и реализуют основной интерфейс для обычной очереди на
# кольцевом буфере. Сами эти операции выполняются за O(1) ибо мы всего лишь осуществляем:
#
# 1a. Проверку текущего размера очереди относительно максимально допустимого размера очереди или
# 1b. Пуста ли очередь сейчас
# 2a. Вставка элемента в конец очереди по сути просто присваивание;
# смещение указателя tail, изменение текущего размера очереди - предсказуемая история O(1)
# 2b. С pop_front всё аналогично
#
# > Интересно получается с push_front. Изначально мозг мне рисовал картинку: "Раз вставлять буду
# в начало, по сути туда, куда указывает head, значит, придется смещать все остальные элементы
# очереди вправо + посмотреть изначально, а не превысили ли мы размер очереди" - O(1) тут не
# пахнет, эта история, как и в обычном массиве, будет O(n). Потом представил в голове:
# "Пусть в случае push_front  указатель head у меня будет выступать tail-ом, в
# конце концов здесь такая же вставка, как и в push_back. Значится, при push_front, я во-первых
# слежу за текущим размером очереди, а вставлять элемент буду на позицию (head - 1) % max_size,
# если она еще не полная." - тут выходит по сложности O(1).
#
# > C pop_back, всё значительно проще:
# "Если очередь не пустая, то я просто беру элемент с позиции (tail - 1 + max_size)) % max_size.
# Знаю, что конструкция x % y в Python всегда возвращает неотрицательный результат, но Python
# для меня не совсем родной язык, поэтому решил перестраховаться (: [я сишник-эмбеддер]
# Модуль здесь нужен для граничных случаев, например, если tail указывает на первый элемент (=0)
# я провалюсь в [max_size - 1] элемент, что ожидаемо. Сложность O(1) таким образом сохраняется.
#
# > Потребление памяти здесь тоже O(1) - определяется пользователем + немного накладных расходов
# для хранения указателей и вспомогательных переменных. Всё предсказуемо
class MyDequeueSized:
    def __init__(self, queue_size):
        self.__queue = [None] * queue_size
        self.__head = 0
        self.__tail = 0
        self.__max_length = queue_size
        self.__queue_size = 0

    def push_back(self, item):
        """Добавление элемента ${item} в конец очереди"""
        if self.__queue_size == self.__max_length:
            # Очередь заполнена
            return None

        # Добавляем элемент в конец очереди
        self.__queue[self.__tail] = item
        # Смещаем указатель на следующую позицию
        self.__tail = (self.__tail + 1) % self.__max_length
        self.__queue_size += 1
        return item

    def push_front(self, item):
        """Добавление элемента ${item} в начало очереди"""
        if self.__queue_size == self.__max_length:
            # Очередь заполнена
            return None

        # Смещаем сначала указатель head на следующую позицию слева
        # Старый элемент на который указывал head, не трогаем
        self.__head = (self.__head - 1 + self.__max_length) % self.__max_length
        self.__queue[self.__head] = item
        self.__queue_size += 1
        return item

    def pop_back(self):
        """Убрать элемент из конца очереди и вернуть его вызывающей стороне"""
        if self.__queue_size == 0:
            # Очередь пуста
            return None

        # Смещаем сначала указатель tail на следующую позицию слева
        # При следующих вставках front, будем использовать его
        # а пока, достанем отсюда значение
        self.__tail = (self.__tail - 1 + self.__max_length) % self.__max_length
        element = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        self.__queue_size -= 1
        return element

    def pop_front(self):
        """Убрать элемент из начала очереди и вернуть его вызывающей стороне"""
        if self.__queue_size == 0:
            # Очередь пуста
            return None

        element = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_length
        self.__queue_size -= 1
        return element

    def get_queue_size(self):
        """Возвращение размера очереди"""
        return self.__queue_size

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
                result = self.push_front(int(args[0]))
                command_output = "error" if result is None else None
            case "push_back":
                result = self.push_back(int(args[0]))
                command_output = "error" if result is None else None
            case "pop_front":
                result = self.pop_front()
                command_output = "error" if result is None else result
            case "pop_back":
                result = self.pop_back()
                command_output = "error" if result is None else result

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
