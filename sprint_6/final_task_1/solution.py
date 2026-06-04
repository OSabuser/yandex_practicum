def read_graph():
    n, m = map(int, input().split())
    edges = []

    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1

        if u == v:  # петли в остов никогда не попадут
            continue

        edges.append((w, u, v))

    return n, edges


def make_dsu(n):
    parent = list(range(n))
    rank = [0] * n
    return parent, rank


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # сжатие пути
    return parent[x]


def union(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        return False  # уже в одной компоненте

    # объединение по рангу
    if rank[root_a] < rank[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a

    if rank[root_a] == rank[root_b]:
        rank[root_a] += 1

    return True


def max_spanning_tree_weight(n, edges):
    """
    Метод Краскала на максимум:
    Сортируем по убыванию веса — жадно берём тяжёлые рёбра
    """
    edges.sort(reverse=True)

    parent, rank = make_dsu(n)

    total_weight = 0
    edges_used = 0

    for w, u, v in edges:
        if union(parent, rank, u, v):
            total_weight += w
            edges_used += 1

    if edges_used == n - 1:
        return total_weight
    else:
        return None  # граф несвязный — остов не существует


if __name__ == "__main__":
    n, edges = read_graph()
    result = max_spanning_tree_weight(n, edges)

    if result is None:
        print("Oops! I did it again")
    else:
        print(result)
