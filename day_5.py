from collections import defaultdict


def get_line_points(line):
    points = []

    x1 = line[0][0]
    y1 = line[0][1]

    x2 = line[1][0]
    y2 = line[1][1]

    dy = 1 if y1 <= y2 else -1
    dx = 1 if x1 <= x2 else -1

    if x1 == x2:
        print(f"process horizontal line: {line}")
        # horizontal line
        while y1 != y2:
            points.append((x1, y1))
            y1 += dy

        points.append((x2, y2))

    elif y1 == y2:
        print(f"process vertical line: {line}")
        # vertical line
        while x1 != x2:
            points.append((x1, y1))
            x1 += dx

        points.append((x2, y2))

    else:
        print(f"process diagonal line: {line}")
        while x1 != x2 and y1 != y2:
            points.append((x1, y1))
            x1 += dx
            y1 += dy

        points.append((x2, y2))

    print(f"points: {points}")

    return points


def _is_horizontal_or_vertical(line):
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        return True
    return False


if __name__ == "__main__":
    with open("day_5_input.txt") as f:
        raw_lines = f.readlines()

    lines = []

    intersections = defaultdict(int)

    for raw in raw_lines:
        line = [(int(v.strip().split(',')[0]), int(v.strip().split(',')[1])) for v in raw.split("->")]
        lines.append(line)

    # bruteforce solution: save all points we have seen in the dictionary and count how many times we have seen them
    for l in lines:
       #if _is_horizontal_or_vertical(l):
            points = get_line_points(l)
            for p in points:
                intersections[f"{p[0]}-{p[1]}"] += 1

    count = len([k for k,v in intersections.items() if v >=2])

    print(count)

