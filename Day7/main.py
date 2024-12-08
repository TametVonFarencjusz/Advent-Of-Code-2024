import itertools
from pprint import pprint


def try_solve(res, nums, signs):
    value = nums[0]
    for i in range(len(nums) - 1):
        if signs[i] == '+':
            value = value + nums[i+1]
        elif signs[i] == '*':
            value = value * nums[i+1]
        elif signs[i] == '|':
            value = int(str(value) + str(nums[i+1]))
    return res == value


sum_value = 0
sum_value2 = 0
data = []
with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    for line in data:
        result = int(line.split(": ")[0])
        numbers = [int(value) for value in line.split(": ")[1].split(" ")]
        for signs in itertools.product("+*", repeat=len(numbers)-1):
            if try_solve(result, numbers, list(signs)):
                sum_value += result
                break
        for signs in itertools.product("+*|", repeat=len(numbers)-1):
            if try_solve(result, numbers, list(signs)):
                sum_value2 += result
                break

print(f"Part One: {sum_value}")
print(f"Part Two: {sum_value2}")


