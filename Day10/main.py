import itertools
from pprint import pprint

with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    grid = [[int(d) for d in list(line)] for line in data]

def go(prev, pos, positions):
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for move in moves:
        if 0 <= pos[0] + move[0] < len(grid) and 0 <= pos[1] + move[1] < len(grid[0]):
            destination = grid[pos[0] + move[0]][pos[1] + move[1]]
            if destination == prev + 1:
                if destination == 9:
                    positions.append((pos[0] + move[0], pos[1] + move[1]))
                else:
                    go(destination, [pos[0] + move[0], pos[1] + move[1]], positions)

starts = []
for _x, line in enumerate(grid):
    _ys = [i for i, X in enumerate(line) if X == 0]
    for _y in _ys:
        starts.append([_x, _y])

score_sum = 0
score_sum2 = 0
for start in starts:
    the_list = []
    go(0, start, the_list)
    score_sum += len(set(the_list))
    score_sum2 += len(the_list)

print(f"Part One: {score_sum}")
print(f"Part One: {score_sum2}")



