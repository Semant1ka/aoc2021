"""
Approach

1) build adjacency list
2) do BFS
3) note path

"""

from collections import defaultdict, deque


def count_paths(text, count_doubles=False):
    adjacency_list = defaultdict(list)

    for line in text.split('\n'):
        conn = line.strip().split('-')

        start = conn[0]
        end = conn[1]

        adjacency_list[start].append(end)
        adjacency_list[end].append(start)

    #print(adjacency_list)

    q = deque()
    q.append(('start', {'start'}, False))

    cnt = 0

    while q:
        # print(q)
        v, seen, seen_twice = q.popleft()

        if v == 'end':
            cnt += 1
            continue

        if v in adjacency_list:
            for adj_v in adjacency_list[v]:
                # if we haven't visited this vertex from this path before visit it
                if adj_v not in seen:
                    updated_seen = set(seen)

                    # if this vertex is in lower case count it as seen, otherwise ignore
                    if adj_v.islower():
                        updated_seen.add(adj_v)

                    q.append((adj_v, updated_seen, seen_twice))
                # only one double visit for lower case vertex is allowed
                # start and end are not allowed to visit twice
                elif adj_v.islower() and not seen_twice and adj_v not in ["start", "end"] and count_doubles:
                    q.append((adj_v, seen, True))

    print(cnt)

    return cnt
