# Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей.
# Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
# Диагональные элементы соседними не считаются.
# Например, в матрице A ( соседними элементами для (0,0) являются 2 и 0, а для (2,1) - 1,2,7,7
#      0 1 2
#   0[ 1 2 3 ]
#   1[ 0 2 6 ]
#   2[ 7 4 1 ]
#   3[ 2 7 0 ]
#
# Соседи в матрице по фон Нейману
# Для элемента A[i[j] его соседями в матрице M*N являются:
# Сверху: A[i-1][j], если i > 0
# Снизу: A[i+1][j], если i < M-1
# Слева: A[i][j-1], если j > 0
# Справа: A[i][j+1], если j < N-1


import sys


class Matrix:
    def __init__(self, row, column, matrix, target):
        self.rows = row
        self.columns = column
        self.matrix = matrix
        self.target = target

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def print_element(self, i, j):
        if i < 0 or i >= self.rows:
            return
        if j < 0 or j >= self.columns:
            return
        print(f"Element: ({i}, {j}) = {self.matrix[i][j]}")

    def get_neighbors_values(self):
        neighbors = []
        # Сверху: A[i-1][j], если i > 0
        if self.target[0] > 0:
            neighbors.append(self.matrix[self.target[0] - 1][self.target[1]])
        # Снизу: A[i+1][j], если i < M-1
        if self.target[0] < self.rows - 1:
            neighbors.append(self.matrix[self.target[0] + 1][self.target[1]])
        # Слева: A[i][j-1], если j > 0
        if self.target[1] > 0:
            neighbors.append(self.matrix[self.target[0]][self.target[1] - 1])
        # Справа: A[i][j+1], если j < N-1
        if self.target[1] < self.columns - 1:
            neighbors.append(self.matrix[self.target[0]][self.target[1] + 1])

        return sorted(neighbors)


def get_matrix():
    # Количество строк и столбцов в матрице
    rows = int(input())
    columns = int(input())

    if rows <= 0 or columns <= 0:
        return
    if rows > 1000 or columns > 1000:
        return

    matrix = []

    # Сборка матрицы
    for _ in range(rows):
        line = sys.stdin.readline().rstrip()
        row_values = list(map(int, line.split()))

        if len(row_values) != columns:
            return
        matrix.append(row_values)

    # Координаты исследуемого элемента
    i = int(input())
    j = int(input())

    if i < 0 or i >= rows:
        return
    if j < 0 or j >= columns:
        return

    return Matrix(rows, columns, matrix, (i, j))


if __name__ == "__main__":
    matrix = get_matrix()
    if matrix is not None:
        neighbors = matrix.get_neighbors_values()
        print(*neighbors)
