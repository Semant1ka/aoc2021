from typing import List


def get_position(positions: List[str]) -> int:
    x, y = 0, 0

    for position in positions:
        _dir, _val = position.split(' ')
        _val = int(_val)

        if _dir == "down":
            y += _val
        elif _dir == "up":
            y -= _val
        elif _dir == "forward":
            x += _val

    return x*y


def get_enhanced_position(positions: List[str]) -> int:
    x, y, aim = 0, 0, 0

    for position in positions:
        _dir, _val = position.split(' ')
        _val = int(_val)

        if _dir == "down":
            aim += _val
        elif _dir == "up":
            aim -= _val
        elif _dir == "forward":
            x += _val
            y += aim * _val

    return x*y


if __name__ == "__main__":
    with open("day_2_input.txt") as f:
        positions = [x for x in f.readlines()]
    print(get_position(positions))
    print(get_enhanced_position(positions))

