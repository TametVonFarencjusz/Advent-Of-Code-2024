def sign(num):
    return -1 if num < 0 else 1 if num > 0 else 0


def report_correct(r):
    subtracted = [int(r[n])-int(r[n+1]) for n in range(len(r)-1)]
    bools = [0 < d * sign(subtracted[0]) < 4 for d in subtracted]
    return bools

data = []
with open('data.txt') as f:
    data = [line.strip() for line in f.readlines()]
    reports = [line.split(" ") for line in data]

counter_1 = 0
counter_2 = 0
for report in reports:
    correction_report = report_correct(report)
    if all(correction_report):
        counter_1 += 1
        counter_2 += 1
    else:
        for i in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(i)
            print(report_copy)
            correction_report_copy = report_correct(report_copy)
            if all(correction_report_copy):
                counter_2 += 1
                break

print(f"Part One: {counter_1}")
print(f"Part Two: {counter_2}")