from collections import deque


def count_fishes_too_long(fishes, days):
    fish_q = deque(fishes)

    for d in range(days):
        print(f"day: {d} , fishes: {len(fish_q)}")
        for f in range(len(fish_q)):
            fish = fish_q.popleft()

            if fish == 0:
                fish_q.append(6)
                fish_q.append(8)
            else:
                fish_q.append(fish-1)

    return len(fish_q)


def count_fishes_fast(fishes, days):
    counts = [0 for _ in range(9)]
    for f in fishes:
        counts[f] +=1

    while days>0:
        counts_next = [0 for _ in range(9)]
        for i in range(9):
            if i == 0:
                counts_next[6] += counts[i]
                counts_next[8] += counts[i]
            else:
                counts_next[i-1] += counts[i]
        days-=1
        counts = counts_next

    return sum(counts)


if __name__ == "__main__":
    with open("day_6_input.txt") as f:
        lines = f.readlines()

    fishes = [int(l) for l in lines[0].strip().split(',')]
    days = 256

    print(count_fishes_fast(fishes, days))
