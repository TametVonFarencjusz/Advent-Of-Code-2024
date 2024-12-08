import re

data = []
with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]

    sum_value = 0
    for line in data:
        found_mul = re.findall(r'mul\([0-9]{,3},[0-9]{,3}\)', line)
        for mul_str in found_mul:
            values = mul_str[4:-1].split(",")
            sum_value += int(values[0]) * int(values[1])

    sum_value2 = 0
    enabled = True
    for line in data:
        found_func = re.findall(r"mul\([0-9]{,3},[0-9]{,3}\)|do\(\)|don't\(\)", line)
        print(found_func)
        for func_str in found_func:
            if func_str == "do()":
                enabled = True
            elif func_str == "don't()":
                enabled = False
            elif enabled:
                values = func_str[4:-1].split(",")
                sum_value2 += int(values[0]) * int(values[1])

print(f"Part One: {sum_value}")
print(f"Part Two: {sum_value2}") #X<83950340
