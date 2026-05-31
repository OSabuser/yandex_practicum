WHITE = "white"
GRAY = "gray"
BLACK = "black"


def create_adjacency_list(vertices, edges):
    adjacency_list = [[] for _ in range(vertices)]

    for _ in range(edges):
        from_vertex, to_vertex = map(int, input().split())
        from_vertex -= 1
        to_vertex -= 1

        adjacency_list[from_vertex].append(to_vertex)

    for i in range(vertices):
        adjacency_list[i].sort()

    return adjacency_list


def dfs_times(adjacency_list, start):
    vertices = len(adjacency_list)

    color = [WHITE] * vertices
    tin = [-1] * vertices
    tout = [-1] * vertices
    timer = 0

    stack = [(start, 0)]  # (вершина, стадия: 0 = вход, 1 = выход)

    while stack:
        vertex, state = stack.pop()

        if state == 0:
            if color[vertex] != WHITE:
                continue

            color[vertex] = GRAY
            tin[vertex] = timer
            timer += 1

            # После обработки всех соседей надо будет выйти из вершины
            stack.append((vertex, 1))

            # Соседей кладём в обратном порядке,
            # чтобы обход шёл по возрастанию номеров
            for neighbor in reversed(adjacency_list[vertex]):
                if color[neighbor] == WHITE:
                    stack.append((neighbor, 0))

        else:
            color[vertex] = BLACK
            tout[vertex] = timer
            timer += 1

    return tin, tout


def main():
    vertices, edges = map(int, input().split())
    adjacency_list = create_adjacency_list(vertices, edges)

    start = 0  # s = 1, внутри программы это индекс 0
    tin, tout = dfs_times(adjacency_list, start)

    for i in range(vertices):
        print(tin[i], tout[i])


if __name__ == "__main__":
    main()
