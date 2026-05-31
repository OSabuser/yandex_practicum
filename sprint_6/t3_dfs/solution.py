WHITE = "white"
GRAY = "gray"
BLACK = "black"


def create_adjacency_list(vertices, edges):
    adjacency_list = [[] for _ in range(vertices)]

    for _ in range(edges):
        u, v = map(int, input().split())
        u -= 1
        v -= 1

        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    for i in range(vertices):
        adjacency_list[i].sort()

    return adjacency_list


def dfs(adjacency_list, start):
    color = [WHITE] * len(adjacency_list)
    traversal_order = []
    stack = [(start, 0)]  # (вершина, стадия)

    while stack:
        vertex, state = stack.pop()

        if state == 0:
            if color[vertex] != WHITE:
                continue

            color[vertex] = GRAY
            traversal_order.append(vertex + 1)

            # После обработки соседей вершина станет чёрной
            stack.append((vertex, 1))

            # Кладём соседей в обратном порядке,
            # чтобы обход шёл по возрастанию
            for neighbor in reversed(adjacency_list[vertex]):
                if color[neighbor] == WHITE:
                    stack.append((neighbor, 0))

        else:
            color[vertex] = BLACK

    return traversal_order


def main():
    vertices, edges = map(int, input().split())
    adjacency_list = create_adjacency_list(vertices, edges)
    start = int(input()) - 1

    traversal_order = dfs(adjacency_list, start)
    print(*traversal_order)


if __name__ == "__main__":
    main()
