def get_input_matrix():
    # Количество клавиш, на которые могут нажать NUMBER_OF_PLAYERS игрока одновременно
    rows = int(input())
    cols = int(input())
    matrix = []

    for _ in range(rows):
        matrix.append(input().split())

    return rows, cols, matrix


if __name__ == "__main__":
    rows, cols, matrix = get_input_matrix()
    print(matrix)
