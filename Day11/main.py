from collections import Counter

with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    stones = Counter(data[0].split(" "))

### PC go brrr###
def do_sth(num):
    if num == '0':
        return ['1']
    elif len(num) % 2 == 0:
        return [str(int(num[:int(len(num)/2)])), str(int(num[int(len(num)/2):]))]
    else:
        return [str(2024 * int(num))]

def do_sth2(num):
    if num == '0':
        return ['1']
    elif len(num) % 2 == 0:
        return [str(int(num[:int(len(num)/2)])), str(int(num[int(len(num)/2):]))]
    else:
        return [str(2024 * int(num))]

### PC go brrr###
# for i in range(25):
#     new_stones = []
#     for stone in stones:
#         new_stones.extend(do_sth(stone))
#     # print(new_stones)
#     print(i)
#     stones = new_stones

for i in range(75):
    new_stones = {}
    for pre_key in stones.keys():
        result = do_sth2(pre_key)
        for key in result:
            if key in new_stones:
                new_stones[key] += stones[pre_key]
            else:
                new_stones[key] = stones[pre_key]
    if i == 25:
        value1 = 0
        for pre_key in stones.keys():
            value1 += stones[pre_key]

    stones = new_stones
print(f"Part One: {value1}")

value2 = 0
for pre_key in stones.keys():
    value2 += stones[pre_key]
print(f"Part Two: {value2}")