class Participant:
    """
    Данные участника соревнования
    """

    def __init__(self, login, solved, penalty):
        self.login = login
        self.solved = solved
        self.penalty = penalty

    def __lt__(self, other):
        """
        Правило сравнения: при сравнении двух участников выше будет идти тот,
        у которого решено больше задач. При равенстве числа решённых задач первым идёт участник
        с меньшим штрафом. Если же и штрафы совпадают, то первым будет тот, у которого логин
        идёт раньше в алфавитном (лексикографическом) порядке.
        """
        if not isinstance(other, Participant):
            raise TypeError

        # Больше решено
        if self.solved != other.solved:
            return self.solved > other.solved
        # Меньше штраф
        if self.penalty != other.penalty:
            return self.penalty < other.penalty
        # Лексикографический порядок раньше (буквы у нас все в нижнем регистре)
        return self.login < other.login


class MyBinHeap:
    def __init__(self):
        self.heap = [-1]

    def push(self, value):
        """Добавление элемента в кучу с просеиванием вверх"""
        self.heap.append(value)
        # Учитываем фиктивный элемент
        index = len(self.heap) - 1
        MyBinHeap.sift_up(heap, index)

    def pop_max(self):
        """Извлечение корневого элемента из кучи с просеиванием вниз"""

        if len(self.heap) - 1 == 0:
            raise IndexError("Heap is empty")

        root_element = self.heap[1]

        # Новый корень дерева - последний элемент
        self.heap[1] = self.heap[-1]
        self.heap.pop()

        # Если в куче ещё остались элементы, восстанавливаем свойство кучи
        if len(self.heap) > 1:
            MyBinHeap.sift_down(self.heap, 1)

        return root_element

    @staticmethod
    def sift_down(heap, idx):
        """
        Просеивание вниз в куче на максимум.

        Args:
            heap: массив, представляющий кучу (индексация с 1, heap[0] фиктивный)
            idx: индекс элемента, от которого начинается просеивание

        Returns:
            int: индекс, на котором элемент оказался после просеивания
        """
        n = len(heap) - 1  # Реальный размер кучи (без фиктивного элемента)

        while True:
            largest = idx  # Изначально считаем текущий элемент максимальным
            left = 2 * idx  # Индекс левого ребёнка
            right = 2 * idx + 1  # Индекс правого ребёнка

            # Проверяем левого ребёнка
            if left <= n and heap[left] > heap[largest]:
                largest = left

            # Проверяем правого ребёнка
            if right <= n and heap[right] > heap[largest]:
                largest = right

            # Если текущий элемент уже максимален среди себя и детей - готово
            if largest == idx:
                break

            # Меняем местами с максимальным ребёнком
            heap[idx], heap[largest] = heap[largest], heap[idx]

            # Продолжаем просеивание с новой позиции
            idx = largest

        return idx

    @staticmethod
    def sift_up(heap, idx):
        """
        Просеивание вверх в куче на максимум.

        Args:
            heap: массив, представляющий кучу (индексация с 1, heap[0] фиктивный)
            idx: индекс элемента, от которого начинается просеивание

        Returns:
            int: индекс, на котором элемент оказался после просеивания
        """

        # Поднимаемся вверх, пока не достигнем корня или не найдем правильное место
        while idx > 1:  # idx=1 это корень, выше подниматься некуда
            parent = idx // 2  # Индекс родителя

            # Если текущий элемент <= родителя, свойство кучи выполнено
            if heap[idx] <= heap[parent]:
                break

            # Меняем местами с родителем (текущий элемент больше)
            heap[idx], heap[parent] = heap[parent], heap[idx]

            # Продолжаем просеивание с позиции родителя
            idx = parent

        return idx


def get_participants_data():
    """
    Ввод данных участников
    """
    n = int(input())
    participants = []
    for _ in range(n):
        login, solved, penalty = input().split()
        participants.append(Participant(login, int(solved), int(penalty)))
    return participants


if __name__ == "__main__":
    heap = MyBinHeap()
    print(heap.heap)
