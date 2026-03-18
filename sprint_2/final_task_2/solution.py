# ССЫЛКА НА ОТЧЁТ: https://contest.yandex.ru/contest/22781/run-report/158623024/
# > //FIXME: Основная идея:
# Кажется достаточно простой и в целом она уже была озвучена в описании к задаче:
# Мы проходим по введённому пользователем выражению, после split()
# 1. Если увидели число (is_valid_operand()), кладем его на вершину стека
# [обращаем внимание на знак]
# 2. Если увидели одну из операций (is_valid_operation()), то выполняем её над двумя верхними
# элементами стека [2xpop()] и кладем результат на вершину стека
# В конце прохода возвращаем значение, лежащее на вершине стека - это и будет результат вычисления.
# Реализацию стека я стащил из задачки №5 про стек.
#
# По поводу сложности:
# Проход по всем элементам выражения: O(N)
# Все операции над стеком: O(1)
# То есть, в целом, временная сложность такого калькулятора O(N)
# По памяти, все зависит от размера стека. Его размер определяется количеством операндов.
# Обычно на одну операцию приходится 2 операнда, думаю что средний размер стека +- N/2,
# т.е. сложность также O(N)


class MyDumbCalculator:
    def __init__(self):
        self.__stack_size = 0
        self.__items = []

    def store_number(self, item):
        """Добавляем ${item} на вершину стека"""
        self.__stack_size += 1
        self.__items.append(item)

    def __pop(self):
        """Забираем элементы с вершины стека"""
        if self.__stack_size == 0:
            return None

        self.__stack_size -= 1
        return self.__items.pop()

    def __get_operands(self):
        """Достать из стека самые последние два операнда для последующего
        использования"""
        # op1, op2 могут быть None
        # Считаем это критической ошибкой
        op1 = self.__pop()
        op2 = self.__pop()

        if op1 is None or op2 is None:
            raise ValueError("Недостаточно операндов в стеке")

        return op1, op2

    def get_result(self):
        """Получить результат вычислений"""
        return self.__pop()

    def perform_operation(self, operator):
        """Выполнить операцию ${operator} над двумя верхними элементами стека
        и положить результат на вершину стека"""
        op2, op1 = self.__get_operands()
        match operator:
            case "+":
                self.store_number(op1 + op2)
            case "-":
                self.store_number(op1 - op2)
            case "*":
                self.store_number(op1 * op2)
            case "/":
                self.store_number(op1 // op2)

    @staticmethod
    def is_valid_operand(maybe_operand):
        """True, если ${maybe_operand} - целое число"""
        try:
            int(maybe_operand)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_operation(maybe_operation):
        """True, если ${maybe_operation} является допустимой арифметической операцией"""
        return maybe_operation in ["+", "-", "*", "/"]


if __name__ == "__main__":
    calculator_sequence: list[str] = input().split()
    calculator_instance = MyDumbCalculator()

    for element in calculator_sequence:
        if MyDumbCalculator.is_valid_operand(element):
            calculator_instance.store_number(int(element))
            continue
        if MyDumbCalculator.is_valid_operation(element):
            calculator_instance.perform_operation(element)

    print(calculator_instance.get_result())
