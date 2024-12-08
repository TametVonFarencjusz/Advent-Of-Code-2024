import itertools
from pprint import pprint


with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    grid = [list(line) for line in data]

    unique = []
    for line in data:
        unique.extend(line)
    unique = set(unique)
    unique.remove('.')
    print(unique)

dictionary = {}
for char in unique:
    positions = []
    for _x, line in enumerate(grid):
        for _y, place in enumerate(line):
            if place == char:
                positions.append([_x, _y])
    dictionary[char] = positions

print(dictionary)


places = []
places2 = []


def find_antinode(two_pos):
    pos = [two_pos[0][0] + (two_pos[0][0] - two_pos[1][0]), two_pos[0][1] + (two_pos[0][1] - two_pos[1][1])]
    if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
        places.append(pos)

def find_antinode2(two_pos):
    for i in range(0, len(grid)):
        pos = [two_pos[0][0] + (two_pos[0][0] - two_pos[1][0]) * i, two_pos[0][1] + (two_pos[0][1] - two_pos[1][1]) * i]
        if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
            places2.append(pos)
        else:
            break

for char in unique:
    for pair in itertools.product(dictionary[char], repeat=2):
        if pair[0] != pair[1]:
            find_antinode(pair)
            find_antinode2(pair)


unique_places = []
[unique_places.append(p) for p in places if p not in unique_places]
print(f"Part One: {len(unique_places)}")


unique_places = []
[unique_places.append(p) for p in places2 if p not in unique_places]
print(f"Part Two: {len(unique_places)}")


