# ССЫЛКА НА ОТЧЁТ: https://contest.yandex.ru/contest/23815/run-report/159514588/
# https://ru.wikipedia.org/wiki/Быстрая_сортировка
# https://otus.ru/journal/sortirovka-hoara-i-drugie-sposoby-sortirovki-massivov/
# 1. Принцип работы быстрой сортировки in-place
#
# 2. Доказательство корректности
#
# 3. Временная сложность
#
# 4. Пространственная сложность
#
import random


class Trainee:
    """
    Данные участника соревнования
    """

    def __init__(self, login, solved, penalty):
        self.login = login
        self.solved = solved
        self.penalty = penalty


def timofeys_sorting_rule(trainee_1, trainee_2):
    """
    Правило сортировки: при сравнении двух участников выше будет  идти тот,
    у которого решено больше задач. При равенстве числа решённых задач первым идёт участник
    с меньшим штрафом. Если же и штрафы совпадают, то первым будет тот, у которого логин
    идёт раньше в алфавитном (лексикографическом) порядке.
    """
    # Больше решено
    if trainee_1.solved != trainee_2.solved:
        return trainee_1.solved > trainee_2.solved

    # Меньше штраф
    if trainee_1.penalty != trainee_2.penalty:
        return trainee_1.penalty < trainee_2.penalty

    # Лексикографический порядок раньше (буквы у нас все в нижнем регистре)
    return trainee_1.login < trainee_2.login


def goes_before(a, b):
    # a идёт раньше b
    return timofeys_sorting_rule(a, b)


def goes_after(a, b):
    # a идёт после b
    return timofeys_sorting_rule(b, a)


def partition_in_place(trainees, left_border, right_border):
    """
    Тут реализуем схему Хоара алгоритма разбиения
    """
    # Хороший вопрос - какого стажёра выбрать в качестве опорного
    # Предоставим это воле случая
    pivot_trainee = trainees[random.randint(left_border, right_border)]
    left_ptr = left_border
    right_ptr = right_border

    while True:
        # Осуществляем свдиг указателей до того момента,
        # пока результаты очередного стажёра не cтанут хуже чем
        # результаты стажёра, выбранного опорным
        while goes_before(trainees[left_ptr], pivot_trainee):
            left_ptr += 1

        # Осуществляем свдиг указателей до того момента,
        # пока результаты очередного стажёра не cтанут лучше чем
        # результаты стажёра, выбранного опорным
        while goes_after(trainees[right_ptr], pivot_trainee):
            right_ptr -= 1

        if left_ptr >= right_ptr:
            return right_ptr  # индекс разделения

        # Меняем местами элементы, имеющие неправильный порядок
        trainees[left_ptr], trainees[right_ptr] = trainees[right_ptr], trainees[left_ptr]
        left_ptr += 1
        right_ptr -= 1


def enhanced_quicksort(trainees, left_border, right_border):
    # Базовый случай: если массив пуст или содержит один элемент
    # Он считается отсортированным
    if left_border >= right_border:
        return trainees

    partition_idx = partition_in_place(trainees, left_border, right_border)
    # Все элементы с индексами <= partition_idx: по порядку расположены не после pivot элемента
    # Все элементы с индексами >= partition_idx + 1: по порядку расположены не до pivot элемента
    # Рекурсивный случай:
    # 1. Сортируем левую половину (<= partition_idx) рекурсивно
    # 2. Сортируем правую половину (>= partition_idx + 1) рекурсивно
    enhanced_quicksort(trainees, left_border, partition_idx)
    enhanced_quicksort(trainees, partition_idx + 1, right_border)

    return trainees


def get_trainees_data():
    n = int(input())
    trainees = []
    for _ in range(n):
        login, solved, penalty = input().split()
        trainees.append(Trainee(login, int(solved), int(penalty)))
    return trainees


if __name__ == "__main__":
    trainees = get_trainees_data()
    sorted_trainees = enhanced_quicksort(trainees, 0, len(trainees) - 1)
    for trainee in sorted_trainees:
        print(trainee.login)
