import itertools
from pprint import pprint


# def can_be_xmas(board, x, y):
#     next_letter = {"X": ["M"], "M": ["A", "X"], "A": ["S", "M"], "S": ["A"]}
#     if board[x][y] in next_letter:
#         found = []
#         for i, j in itertools.product(range(-1, 2), range(-1, 2)):
#             if i != 0 or j != 0:
#                 if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
#                     if board[x+i][y+j] in next_letter[board[x][y]] and board[x+i][y+j] not in found:
#                         found.append(board[x+i][y+j])
#                     # if len(found) == len(next_letter[board[x][y]]):
#                     #     break
#         if len(found) != len(next_letter[board[x][y]]):
#             print(found)
#             board[x][y] = '.'


def can_be_xmas(board, x, y):
    counter = 0
    if board[x][y] == "M":
        for i, j in itertools.product(range(-1, 2), range(-1, 2)):
            if i != 0 or j != 0:
                if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]) \
                        and 0 <= x - i < len(board) and 0 <= y - j < len(board[0]) \
                        and 0 <= x - 2*i < len(board) and 0 <= y - 2*j < len(board[0]):

                    if board[x+i][y+j] == "X" and board[x-i][y-j] == "A":
                        if board[x-i*2][y-j*2] == "S":
                            counter += 1
    return counter


def can_be_x_mas(board, x, y):
    local_counter = 0
    if board[x][y] == "A":
        for i, j in itertools.product(range(-1, 2), range(-1, 2)):
            if i != 0 and j != 0:
                if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]) \
                        and 0 <= x - i < len(board) and 0 <= y - j < len(board[0]):

                    if board[x+i][y+j] == "M" and board[x-i][y-j] == "S":
                        local_counter += 1
    return 1 if local_counter == 2 else 0


data = []
with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    grid = [list(line) for line in data]

xmas_counter = 0
for _x, _y in itertools.product(range(0, len(grid[0])), range(0, len(grid[1]))):
    xmas_counter += can_be_xmas(grid, _x, _y)
print(f"Part One: {xmas_counter}")

x_mas_counter = 0
for _x, _y in itertools.product(range(0, len(grid[0])), range(0, len(grid[1]))):
    x_mas_counter += can_be_x_mas(grid, _x, _y)
print(f"Part One: {x_mas_counter}")
