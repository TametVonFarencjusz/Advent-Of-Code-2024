import itertools
from pprint import pprint

with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    nums = list(data[0])

big_list = []
digit = 0
for i, d in enumerate(nums):
    if i % 2 == 0:
        print(d)
        big_list.extend([digit] * int(d))
        digit = digit+1
    else:
        big_list.extend(["."] * int(d))
# print(big_list)

only_ids = [d for d in big_list if d != "."]
only_ids2 = [d for d in big_list if d != "."]
# print(only_digits)

line = [d if d != "." else only_ids.pop() for d in big_list]
# print("".join(line[:len(only_digits2)]))

filesystem = line[:len(only_ids2)]

check_sum = 0
for i, d in enumerate(filesystem):
    check_sum += i * int(d)
print(f"Part One: {check_sum}")

# Part Two
big_list = []
digit = 0
for i, d in enumerate(nums):
    if i % 2 == 0:
        print(d)
        big_list.extend([[str(digit)] * int(d)])
        digit = digit+1
    else:
        if int(d) > 0:
            big_list.extend(["." * int(d)])
print(big_list)

def find_first_space(size):
    for i, ele in enumerate(big_list):
        if '.' in ele and len(ele) >= size:
            return i
    return -1

def replace_free_space(index, file, file_index):
    if len(big_list[index]) > len(file):
        big_list[index] = big_list[index][len(file):]

        big_list[file_index] = '.' * len(file)
        big_list.insert(index, file)
        return 1
    else:
        big_list[index] = file
        big_list[file_index] = '.' * len(file)
        return 0

def connect_dots():
    j = 0
    while j < len(big_list)-1:
        if '.' in big_list[j] and '.' in big_list[j+1]:
            big_list[j] += big_list.pop(j+1)
        else:
            j += 1

i = len(big_list) - 1
while i >= 0:
    if "." not in big_list[i]:
        idx = find_first_space(len(big_list[i]))
        if idx != -1 and idx < i:
            i += replace_free_space(idx, big_list[i], i)
            connect_dots()
    i -= 1
print(big_list)

extracted_list = []
for ele in big_list:
    if '.' in ele:
        extracted_list.extend([0] * len(ele))
    else:
        extracted_list.extend(ele)

check_sum = 0
for i, d in enumerate(extracted_list):
    check_sum += i * int(d)
print(f"Part Two: {check_sum}")
