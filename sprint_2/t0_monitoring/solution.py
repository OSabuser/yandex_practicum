class Matrix:
    def __init__(self, rows, cols, matrix):
        self.rows = rows
        self.cols = cols
        self.data = matrix


def get_input_matrix():
    rows = int(input())
    cols = int(input())
    matrix = []

    for _ in range(rows):
        matrix.append(input().split())

    return Matrix(rows, cols, matrix)


if __name__ == "__main__":
    matrix = get_input_matrix()

    # Подготовка транспонированной матрицы
    transported_matrix = Matrix(
        matrix.cols, matrix.cols, [[None for _ in range(matrix.rows)] for _ in range(matrix.cols)]
    )

    # Банально и просто, сложность O(n^2) - можно заполнять матрицу прямо в рантайме
    # в момент заполнения исходной
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            transported_matrix.data[j][i] = matrix.data[i][j]

    for row in transported_matrix.data:
        print(*row)
