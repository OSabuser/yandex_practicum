# ССЫЛКА НА ОТЧЁТ: https://contest.yandex.ru/contest/26133/run-report/163550987/
#
# 1. Принцип работы алгоритма
#
# Вдохновлялся:
# 1. https://medium.com/@iamhappycoder/leetcode-394-decode-string-6c78670ef7af
# 2. https://algo.monster/liteproblems/394
# 3. https://algo.monster/liteproblems/14
# 4. https://ruslanspivak.com/lsbasi-part7/
# 5. https://realpython.com/introduction-to-python-generators/
#
# Задача состоит из двух этапов: ленивая распаковка через рекурсивные генераторы
# и поиск наибольшего общего префикса
#
# > Вычисление происходит следующим образом:
#
# 1. Ленивая распаковка:
# - Функция decompress работает как ленивый генератор, принимая исходную строку
# - Чтобы не тратить время на поиск закрывающих скобок `]` при каждой итерации,
# мы используем предвычисленный словарь jump_table. Без его использования
# decompress на yield'ах работал очень медленно, ловил ошибки TL на проверяющей
# платофрме.
# - С помощью yield from алгоритм рекурсивно выдает символы.
#
# 2. Поиск префикса:
# - Читаем строки, создаем генераторы.
# - Синхронно сравниваем потоки через zip. Вспомогательная функция get_common_prefix_len
# ограничивает длину проверки текущим максимумом lcp_length,
# чтобы не распаковывать лишние символы.
#
# 2. Доказательство корректности
#
# А. Корректность распаковки
# - Словарь jump_table, созданный через стек, гарантированно хранит точные
# индексы парных скобок с учетом любой вложенности. Конструкция
# for _ in range(num): yield from... в точности раскрывает выражение n[A].
#
# Б. Корректность поиска наибольшего общего префикса
# - Общий префикс обладает свойством ассоциативности: lcp(s1, s2, s3) = lcp(lcp(s1, s2), s3).
# - Попарное вычисление для всех строк дает глобальный результат.
#
# 3. Временная сложность
#
# - Предрасчет jump_table: O(S_i) для каждой сжатой строки.
# - Распаковка и сравнение: на каждой итерации сравниваются два генератора.
# Благодаря раннему выходу (if match_len == max_len: break) мы никогда не
# распаковываем больше символов, чем lcp_length.
# В худшем случае это O(L_max), где L_max <= 10^5 - максимальная длина распакованной строки.
#
# Итоговая временная сложность ограничена O(n * L_max) = 1000 * 10^5 = 10^8 операциями.
#
# - Итого на одну итерацию цикла: O(S_i) + O(L_i) + O(L_i) = O(L_i), так как S_i <= L_i.
#
# Итоговая временная сложность для всех n запакованных строк:
# O(L_1) + O(L_2) + ... + O(L_n) = O(SUM(L_i)).
#
#
# 4. Пространственная сложность
#
# - словарь jump_table занимает память пропорционально количеству скобок O(S_i)
# - Генераторы потребляют память только под стек вызовов
# - В памяти одновременно находятся две исходные строки O(S_max)
# - Финальная строка-ответ: O(L_max)
#
# Итоговая пространственная сложность: O(S_max + L_max).


def get_jump_table(packed_str: str) -> dict:
    """
    Предвычисляет индексы закрывающих скобок,
    возвращает словарь {индекс_открывающей: индекс_закрывающей}.
    """
    jump = {}
    stack = []
    for i, char in enumerate(packed_str):
        if char == "[":
            stack.append(i)
        elif char == "]":
            jump[stack.pop()] = i
    return jump


def decompress(packed_str: str, jump_table: dict, start: int = 0, end: int = None):
    """
    Ленивый генератор, распаковывающий строку с использованием таблицы переходов.
    """
    if end is None:
        end = len(packed_str)

    i = start
    while i < end:
        char = packed_str[i]

        if char.isdigit():
            num = int(char)
            # '[' всегда идет сразу после однозначного числа
            bracket_idx = i + 1
            inner_start = bracket_idx + 1
            inner_end = jump_table[bracket_idx]

            # Рекурсивно делегируем выдачу символов внутреннего блока num раз
            for _ in range(num):
                yield from decompress(packed_str, jump_table, inner_start, inner_end)

            # Прыгаем сразу за закрывающую скобку
            i = inner_end + 1
        else:
            yield char
            i += 1


def get_common_prefix_len(gen1, gen2, max_len) -> int:
    """
    Сравнивает два потока символов и возвращает длину их совпадения.
    Останавливается досрочно, если достигнут текущий максимум совпадения.
    """
    match_len = 0
    for c1, c2 in zip(gen1, gen2, strict=False):
        # max_len может быть None для первой проверки
        if max_len is not None and match_len == max_len:
            break

        if c1 == c2:
            match_len += 1
        else:
            break

    return match_len


def main():

    n = int(input().strip())

    first_packed = input().strip()
    jump1 = get_jump_table(first_packed)

    # None означает, что длина префикса пока не ограничена
    lcp_length = None

    # Сравниваем со всеми остальными строками
    for _ in range(2, n + 1):
        # Ранний выход, если общий префикс уже пуст
        if lcp_length == 0:
            break

        next_packed = input().strip()
        jump2 = get_jump_table(next_packed)

        gen1 = decompress(first_packed, jump1)
        gen2 = decompress(next_packed, jump2)

        # Вычисляем новую длину совпадения
        lcp_length = get_common_prefix_len(gen1, gen2, lcp_length)

    # Собираем финальную строку-ответ
    if lcp_length == 0:
        print("")
    else:
        result = []
        for c in decompress(first_packed, jump1):
            if lcp_length is not None and len(result) == lcp_length:
                break
            result.append(c)
        print("".join(result))


if __name__ == "__main__":
    main()
