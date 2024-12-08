from itertools import permutations

data = []
with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    rules_data = [line.split("|") for line in data if '|' in line]
    updates_data = [line.split(",") for line in data if ',' in line]

rules = [[int(line[0]), int(line[1])] for line in rules_data]
updates = [[int(number) for number in line] for line in updates_data]

print(rules)
print(updates)

passed_sum = 0
failed_sum = 0

for i, update in enumerate(updates):
    failed = False
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                failed = True
                break
    if not failed:
        passed_sum += update[int((len(update)-1) / 2)]
    else:
        passed = False
        while not passed:
            passed = True
            for rule in rules:
                if rule[0] in update and rule[1] in update:
                    smaller_index = update.index(rule[0])
                    bigger_index = update.index(rule[1])
                    if smaller_index > bigger_index:
                        value = update.pop(smaller_index)
                        update.insert(bigger_index, value)
                        passed = False
        failed_sum += update[int((len(update)-1) / 2)]
        #IT'S SLOW
        # for state in permutations(update):
        #     failed = False
        #     for rule in rules:
        #         if rule[0] in state and rule[1] in state:
        #             if state.index(rule[0]) > state.index(rule[1]):
        #                 failed = True
        #                 break
        #     if not failed:
        #         failed_sum += state[int((len(state)-1) / 2)]
        #         break

print(f"Part One: {passed_sum}")
print(f"Part Two: {failed_sum}")
