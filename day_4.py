"""
Approach #1: brute force
for each number in the draw
check it in each board
check if this board wins

T(n) = O(n -> inf) * O(m) * 25

# optimization #1
for each board: all_numbers_set, explored_numbers_set, board, visited

{num: (position}}
"""

def play_bingo(boards, input):
    for val in input:
        winning_boards = []
        for j in range(len(boards)):
            # check for value on the board
            if val in boards[j].board:
                boards[j].seen_nums.add(val)
                row, col = boards[j].board[val]
                boards[j].visited[row][col] = True
                # check for win
                if all(boards[j].visited[row]) or all([x[col] for x in boards[j].visited]):
                    if len(boards) == 1:
                        mult = set(boards[j].board.keys()) - boards[j].seen_nums
                        return sum([int(x) for x in mult if x]) * int(val)
                    else:
                        winning_boards.append(boards[j])

        for num in winning_boards:
            boards.remove(num)



class Board:
    def __init__(self):
        self.seen_nums = set()
        self.board = {}
        self.visited = [[False for _ in range(5)] for _ in range(5)]


if __name__ == "__main__":
    with open("day_4_input.txt") as f:
        lines = f.readlines()
    inpt = lines[0].strip().split(",")
    boards = []
    board = None
    current_row = -1

    for i in range(1, len(lines)):

        if len(lines[i]) < 2:
            # add previous board to list
            if board:
                boards.append(board)
            # start new board after new line
            board = Board()
            current_row = 0
        else:
            vals = [x for x in lines[i].strip().split(" ") if x]
            for j in range(5):
                board.board.update({vals[j].strip(): (current_row, j)})
            current_row += 1

    if board:
        boards.append(board)

    print(play_bingo(boards, inpt))



