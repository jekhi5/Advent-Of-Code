lines = open("/Users/jacobkline/coding/Advent of Code/2018/Day 1 - Chronal Calibration/input.txt").readlines()
print("Part one: ", sum(list(map(lambda char: int(char), lines))))

lines = list(map(lambda char: int(char), lines))

incrementalTotals = []
total = 0
curIndex = 0
while True:
    total += lines[curIndex % len(lines)]
    if total in incrementalTotals: break
    else: incrementalTotals.append(total)
    curIndex += 1

print("Part two: ", total)
