# ССЫЛКА НА ОТЧЁТ: https://contest.yandex.ru/contest/22450/run-report/157830565/
# > Основная идея - решать "в лоб":
# 1. Собрать 4 строки в одну единую строку
# 2. Создать массив из 9 элементов:
# - каждый элемент соответствует количеству встречающихся цифр от 1 до 9
# - индексы массива соответствуют значению числа  n - 1
# Пройтись по строке, считая количество тех или иных цифр, игнорируя точки:
# ```
# если символ != точка:
#   массив[символ-1] += 1
# ```
# 3. Посчитать количество "доступных пальцев" игроков = 2*k
# 4. Пройтись по полученному в п.2 массиву, считая количество баллов:
# ```
# если массив[элемент] != 0:
#   если доступных пальцев >= массив[элемент]:
#       прибавляем очко
# ```


# Количество игроков в "Тренажёр скоростной печати"
NUMBER_OF_PLAYERS = 2

# Количество рядов клавиш в тренажёре (1 ряд = 4 клавиши)
ROWS_IN_GAMEFIELD = 4

# Символ, который может присутствовать на игровом поле
EMPTY_KEY_CHAR = "."


def get_input_values():
    # Количество клавиш, на которые могут нажать NUMBER_OF_PLAYERS игрока одновременно
    available_fingers = NUMBER_OF_PLAYERS * int(input())
    current_keys_str = ""

    for _ in range(ROWS_IN_GAMEFIELD):
        current_keys_str += input()

    return available_fingers, current_keys_str


# Получение списка количества встречающихся цифр на игровом поле
def get_numbers_occurences(current_keys_str: str):
    count_of_keys = [0] * 9

    for char in current_keys_str:
        if char != EMPTY_KEY_CHAR:  # Тут конечно сам бог велел использовать isdigit() (:
            count_of_keys[int(char) - 1] += 1

    return count_of_keys


# Получение общего количества очков, набранных Гошей и Тимофеем
def get_max_points_value(available_fingers: int, current_keys_str: str):
    count_of_keys = get_numbers_occurences(current_keys_str)
    points = 0
    for key in count_of_keys:
        if key != 0:
            if available_fingers >= key:
                points += 1
    return points


if __name__ == "__main__":
    available_fingers, current_keys_str = get_input_values()
    points = get_max_points_value(available_fingers, current_keys_str)
    print(points)
