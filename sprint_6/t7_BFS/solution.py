from collections import deque


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


def bfs(adjacency_list, start):
    n = len(adjacency_list)
    visited = [False] * n
    order = []

    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        order.append(vertex + 1)  # обратно в 1-based

        for neighbor in adjacency_list[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return order


def main():
    vertices, edges = map(int, input().split())
    adjacency_list = create_adjacency_list(vertices, edges)
    start = int(input()) - 1

    order = bfs(adjacency_list, start)
    print(*order)


if __name__ == "__main__":
    main()
