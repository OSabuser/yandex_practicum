def read_grid():
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    return n, m, grid


def explore_island(start_i, start_j, grid, visited, n, m):
    stack = [(start_i, start_j)]
    visited[start_i][start_j] = True
    size = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        i, j = stack.pop()
        size += 1

        for di, dj in directions:
            ni = i + di
            nj = j + dj

            if 0 <= ni < n and 0 <= nj < m:
                if grid[ni][nj] == "#" and not visited[ni][nj]:
                    visited[ni][nj] = True
                    stack.append((ni, nj))

    return size


def count_islands_and_max_size(n, m, grid):
    visited = [[False] * m for _ in range(n)]
    islands_count = 0
    max_size = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#" and not visited[i][j]:
                islands_count += 1
                current_size = explore_island(i, j, grid, visited, n, m)

                if current_size > max_size:
                    max_size = current_size

    return islands_count, max_size


if __name__ == "__main__":
    n, m, grid = read_grid()
    islands_count, max_size = count_islands_and_max_size(n, m, grid)
    print(islands_count, max_size)
