'''
Approach #1:
For each step:

1) increase each value by 1
2) if value => 10 put this index into a flash queue, and mark as flashed
3) do DFS/BFS and flush all other values
4) reset flash table

'''

from collections import deque

DIRS = [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (-1, 1),(1,1),(1,-1)]

SIZE = 10

STEPS = 200


def try_flash(i, j, octo_map, q, flashed, cnt):
    if not flashed[i][j]:
        octo_map[i][j] += 1
        if octo_map[i][j] > 9:
            octo_map[i][j] = 0
            flashed[i][j] = True
            for d in DIRS:
                d_i = i + d[0]
                d_j = j + d[1]

                if 0 <= d_i < 10 and 0 <= d_j < 10:
                    q.append((d_i, d_j))

            return 1

    return 0


def model(octo_map):
    cnt = 0
    k = 0

    while True:
        q = deque()

        # we could reuse these but whatever
        flashed = [[False for _ in range(SIZE)] for _ in range(SIZE)]

        for i in range(SIZE):
            for j in range(SIZE):
                cnt += try_flash(i, j, octo_map, q, flashed, cnt)

        while q:
            y, x = q.popleft()
            cnt += try_flash(y, x, octo_map, q, flashed, cnt)

        #print(f"Step {k+1}")
        # for o in octo_map:
        #     print(f"{o}")

        import itertools
        if all(list(itertools.chain.from_iterable(flashed))):
            return k + 1

        k+=1

if __name__ == '__main__':
    octo_map = []
    with open("day_11_input.txt") as f:
        for line in f.readlines():
            octo_map.append([int(c) for c in line.strip()])

    print(model(octo_map))
