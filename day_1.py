from typing import List


def count_increases(depths: List[int]) -> int:
    if len(depths) < 2:
        return 0

    cnt = 0

    for i in range(len(depths)-1):
        if depths[i+1] > depths[i]:
            cnt += 1

    return cnt


def count_window_increases(depths: List[int]) -> int:
    if len(depths) < 6:
        return 0

    prev_sum = -1
    cnt = 0

    for i in range(len(depths)-2):
        current_sum = sum(depths[i:i+3])

        if prev_sum != -1:
            if current_sum > prev_sum:
                cnt += 1
        prev_sum = current_sum

    return cnt


if __name__ == "__main__":
    with open("depth.txt") as f:
        depths = [int(x) for x in f.readlines()]
    print(count_increases(depths))
    print(count_window_increases(depths))






