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

    for i in range(vertices):
        adjacency_list[i].sort()

    return adjacency_list


def dfs_topo_from_vertex(adjacency_list, start, color, topo_order):
    # стек: (вершина, стадия: 0 = вход, 1 = выход)
    stack = [(start, 0)]

    while stack:
        vertex, state = stack.pop()

        if state == 0:
            if color[vertex] != WHITE:
                continue

            color[vertex] = GRAY

            # После обработки всех детей надо "выйти" из вершины
            stack.append((vertex, 1))

            # Соседей кладём в обратном порядке, чтобы
            # DFS шёл по возрастанию номеров
            for neighbor in reversed(adjacency_list[vertex]):
                if color[neighbor] == WHITE:
                    stack.append((neighbor, 0))

        else:
            color[vertex] = BLACK
            topo_order.append(vertex + 1)  # 1-based для вывода


def topological_sort(adjacency_list):
    n = len(adjacency_list)
    color = [WHITE] * n
    topo_order = []

    for v in range(n):
        if color[v] == WHITE:
            dfs_topo_from_vertex(adjacency_list, v, color, topo_order)

    topo_order.reverse()
    return topo_order


def main():
    vertices, edges = map(int, input().split())
    adjacency_list = create_adjacency_list(vertices, edges)
    topo_order = topological_sort(adjacency_list)
    print(*topo_order)


if __name__ == "__main__":
    main()
