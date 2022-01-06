"""
Approach:
1) define a grid, set all values to 0
2) parse input and set relevant 0 to 1
3) if fold is horizontal:
    for each dot with y > fold_y:
        diff = y - fold_y
        set new dot -> new_y = fold_y - diff

  if fold is vertical:
     for each x > x_fold:
        diff = x - x_fold
        set new dot -> new_x = x_fold - diff

4) count all dots up to fold line (will be just a sum of all values in the columns/rows)

"""


def count_dots(dots, instructions):
    max_x = max(dots, key=lambda x: x[0])[0] + 1
    max_y = max(dots, key=lambda y: y[1])[1] + 1

    # add +1 because we want to include the dots with the largest coordinates into the paper
    paper = [[0 for _ in range(max_x)] for _ in range(max_y)]

    for dot in dots:
        x = dot[0]
        y = dot[1]
        paper[y][x] = 1

    # for p in paper:
    #     print(p)

    for inst in instructions:
        axis, value = inst.split('=')
        value = int(value)
        print(f"axis = {axis}, value = {value}")

        if axis == 'y':
            for y in range(value+1, max_y):
                # start looking that Y > Y fold
                for x in range(max_x):
                    if paper[y][x] == 1:
                        diff = y - value
                        new_y = value - diff
                        paper[new_y][x] = 1
                        paper[y][x] = 0
        else:
            for x in range(value+1, max_x):
                for y in range(max_y):
                    if paper[y][x] == 1:
                        diff = x - value
                        new_x = value - diff
                        paper[y][new_x] = 1
                        paper[y][x] = 0



        #print(sum([sum(column) for column in paper]))

    #print(f"max x = {max_x}, max_y = {max_y}")
    for p in paper:
        print(p)





if __name__ =="__main__":
    with open("day_13_input.txt") as f:
        lines = f.readlines()

    dots = []
    instructions = []

    for i in range(len(lines)):
        if ',' in lines[i]:
            dots.append([int(x) for x in lines[i].strip().split(',')])
        elif '=' in lines[i]:
            instructions.append(lines[i].strip().split(' ')[2])

    count_dots(dots, instructions)




