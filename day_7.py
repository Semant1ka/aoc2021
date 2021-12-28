from statistics import median, mean


def get_answer_part1(positions):
    med = int(median(positions))
    return sum([abs(med-x) for x in positions])


def get_answer_part2(positions):
    m = int(mean(positions))
    return sum([(abs(m - x)*(abs(m - x)+1))/2 for x in positions])


if __name__ == "__main__":
    with open("day_7_input.txt") as f:
        lines = f.readlines()

    positions = [int(l) for l in lines[0].strip().split(",")]
    print(get_answer_part2(positions))
