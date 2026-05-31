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


def dfs(adjacency_list, start, color, component_count):
    stack = [start]

    while stack:
        vertex = stack.pop()

        if color[vertex] != -1:
            continue

        color[vertex] = component_count

        # Кладём соседей в обратном порядке,
        # чтобы обход шёл по возрастанию
        for neighbor in reversed(adjacency_list[vertex]):
            if color[neighbor] == -1:
                stack.append(neighbor)


def find_connected_components(adjacency_list):
    vertices = len(adjacency_list)
    color = [-1] * vertices
    component_count = 0

    for vertex in range(vertices):
        if color[vertex] == -1:
            component_count += 1
            dfs(adjacency_list, vertex, color, component_count)

    components = [[] for _ in range(component_count)]

    for vertex in range(vertices):
        component_number = color[vertex]
        components[component_number - 1].append(vertex + 1)

    return component_count, components


def main():
    vertices, edges = map(int, input().split())
    adjacency_list = create_adjacency_list(vertices, edges)

    component_count, components = find_connected_components(adjacency_list)

    print(component_count)
    for component in components:
        print(*component)


if __name__ == "__main__":
    main()
