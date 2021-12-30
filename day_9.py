import math
from collections import deque


def get_risk_level(height_map):
    total = 0
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            if is_minimum(i, j, height_map):
                total += height_map[i][j] + 1

    return total


def get_largest_basins(height_map):
    result = []
    visited = [[False for _ in range(len(height_map[x]))] for x in range(len(height_map))]

    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            if is_minimum(i, j, height_map):
                size = 0
                # use BFS to find all the values
                q = deque()
                q.append((i, j))
                visited[i][j] = True

                while q:
                    y, x = q.popleft()
                    size += 1

                    height = len(height_map)
                    width = len(height_map[y])

                    for d in DIR:
                        d_i = y + d[0]
                        d_j = x + d[1]

                        if 0 <= d_i < height and 0 <= d_j < width and height_map[d_i][d_j]!= 9 and not visited[d_i][d_j]:
                            q.append((d_i, d_j))
                            visited[d_i][d_j] = True

                result.append(size)

    # multiply top 3
    return math.prod(sorted(result, reverse=True)[:3])

DIR = [(-1,0), (1,0), (0,1), (0,-1)]


def is_minimum(i, j, height_map):
    height = len(height_map)
    width = len(height_map[i])

    neighbors = []

    for d in DIR:
        d_i = i + d[0]
        d_j = j + d[1]

        if 0 <= d_i < height and 0 <= d_j < width:
            neighbors.append(height_map[d_i][d_j])

    return height_map[i][j] < min(neighbors)


if __name__ == '__main__':
    height_map = []
    with open("day_9_input.txt") as f:
        for line in f.readlines():
            height_map.append([int(c) for c in line.strip()])

    print(get_largest_basins(height_map))

