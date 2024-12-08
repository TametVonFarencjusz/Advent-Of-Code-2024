data = []
with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    values = [line.split("   ") for line in data]
    left = [int(value[0]) for value in values]
    right = [int(value[1]) for value in values]

left.sort()
right.sort()

distances = [abs(left[i]-right[i]) for i in range(len(left))]

print(f"Part One: {sum(distances)}")

counter = 0
for number in left:
    counter += number * right.count(number)
print(f"Part Two: {counter}")