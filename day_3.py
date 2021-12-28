# can this be solved with binary operations? probably yes :/
from collections import deque


def _get_values(report):
    # this is way too brute force :/
    if not report:
        return

    ones = [0 for _ in range(len(report[0]))]
    zeros = [0 for _ in range(len(report[0]))]

    for line in report:
        for i in range(len(line)):
            if line[i] == '1':
                ones[i] += 1
            else:
                zeros[i] += 1

    # we can return array with most popular value, the opposite will ne least popular
    return ones, zeros


def get_power_consumption(report):
    ones, zeros = _get_values(report)
    gamma, epsilon = "", ""

    for i in range(len(report[0])):
        gamma += "1" if ones[i] > zeros[i] else "0"
        epsilon += "1" if ones[i] < zeros[i] else "0"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon


def get_life_support_rating(report):
    q = deque(report)

    # get oxygen generator
    current_index = 0

    while len(q) > 1:
        ones, zeros = _get_values(q)
        size = len(q)
        for i in range(size):
            val = q.popleft()
            if (ones[current_index] >= zeros[current_index]) and val[current_index] == "1":
                q.append(val)
            elif (ones[current_index] < zeros[current_index]) and val[current_index] == "0":
                q.append(val)
        current_index += 1

    oxygen_generator_rating = int(q[0], 2)

    # get co2 rating
    q = deque(report)
    current_index = 0
    while len(q) > 1:
        ones, zeros = _get_values(q)
        size = len(q)
        for i in range(size):
            val = q.popleft()
            if (ones[current_index] >= zeros[current_index]) and val[current_index] == "0":
                q.append(val)
            elif (ones[current_index] < zeros[current_index]) and val[current_index] == "1":
                q.append(val)
        current_index += 1

    co2_rating = int(q[0], 2)

    return co2_rating * oxygen_generator_rating


if __name__ == "__main__":
    with open("day_3_input.txt") as f:
        report = [x.strip() for x in f.readlines()]
#         report = ["00100",
# "11110",
# "10110",
# "10111",
# "10101",
# "01111",
# "00111",
# "11100",
# "10000",
# "11001",
# "00010",
# "01010"]
        print(get_power_consumption(report))
        print(get_life_support_rating(report))
