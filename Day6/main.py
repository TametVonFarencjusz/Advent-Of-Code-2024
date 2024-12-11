import itertools
from pprint import pprint

data = []
with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    grid = [list(line) for line in data]


def guard_move(board, x, y, d):
    dir = {"^": [-1, 0], "v": [1, 0], ">": [0, 1], "<": [0, -1]}
    next = ["^", ">", "v", "<"]

    i = dir[d][0]
    j = dir[d][1]
    if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
        if board[x+i][y+j] == "#":
            return [True, x, y, next[((next.index(d) + 1) % len(next))]]
        else:
            board[x][y] = 'X'
            return [True, x + i, y + j, d]
    else:
        board[x][y] = 'X'
        return [False]


def guard_move2(board, x, y, d):
    dir = {"^": [-1, 0], "v": [1, 0], ">": [0, 1], "<": [0, -1]}
    next = ["^", ">", "v", "<"]

    i = dir[d][0]
    j = dir[d][1]
    if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
        if board[x+i][y+j] == "#":
            return [True, x, y, next[((next.index(d) + 1) % len(next))]]
        else:
            if board[x][y] in ['.', '^']:
                board[x][y] = [d]
            else:
                if d in board[x][y]:
                    return [False, "LOOP"]
                board[x][y].append(d)

            return [True, x + i, y + j, d]
    else:
        board[x][y] = d
        return [False, "END"]


for _x, line in enumerate(data):
    if "^" in line:
        _y = line.index("^")
        go = [True, _x, _y, "^"]
        while go[0]:
            go = guard_move(grid, go[1], go[2], go[3])
counter = 0
for line in grid:
    counter += line.count("X")

print(f"Part One: {counter}")

Xs = []
for _x, line in enumerate(grid):
    _ys = [i for i, X in enumerate(line) if X == "X"]
    for _y in _ys:
        Xs.append([_x, _y])
print(Xs)

for _x, line in enumerate(data):
    if "^" in line:
        _y = line.index("^")
        _XS, _YS = _x, _y

counter2 = 0
for _xO, _yO in Xs:
    grid2 = [list(line) for line in data]
    if _xO != _XS or _yO != _YS:
        grid2[_xO][_yO] = "#"

        go = [True, _XS, _YS, "^"]
        while go[0]:
            go = guard_move2(grid2, go[1], go[2], go[3])
        if go[1] == "LOOP":
            counter2 += 1

print(f"Part Two: {counter2}")
