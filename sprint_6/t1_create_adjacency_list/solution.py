def create_adjacency_list():
    vertices, edges = map(int, input().split())
    adjacency_list = [[] for _ in range(vertices)]

    for _ in range(edges):
        # Считываем ребро
        u, v = map(int, input().split())
        # Индексация с нуля
        u -= 1
        adjacency_list[u].append(v)

    for i in range(vertices):
        # Сортируем номера вершин по возрастанию
        neighbors = sorted(adjacency_list[i])
        # Формат: число связанных вершин + номера вершин по возрастанию
        line = [str(len(neighbors))] + [str(v) for v in neighbors]
        print(" ".join(line))


if __name__ == "__main__":
    create_adjacency_list()
