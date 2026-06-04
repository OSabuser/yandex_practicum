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


def bfs_max_distance(adjacency_list, start):
    n = len(adjacency_list)
    dist = [-1] * n

    queue = deque()
    queue.append(start)
    dist[start] = 0

    while queue:
        vertex = queue.popleft()

        for neighbor in adjacency_list[vertex]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[vertex] + 1
                queue.append(neighbor)

    return max(dist)


def main():
    vertices, edges = map(int, input().split())
    adjacency_list = create_adjacency_list(vertices, edges)
    s = int(input()) - 1

    answer = bfs_max_distance(adjacency_list, s)
    print(answer)


if __name__ == "__main__":
    main()
