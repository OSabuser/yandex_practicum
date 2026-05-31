def create_adjacency_matrix():
    vertices, edges = map(int, input().split())
    adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    # Заполнение матрицы смежности (изначально все нули)
    for _ in range(edges):
        u, v = map(int, input().split())
        adjacency_matrix[u - 1][v - 1] = 1

    for vertice in adjacency_matrix:
        print(*vertice)


if __name__ == "__main__":
    create_adjacency_matrix()
