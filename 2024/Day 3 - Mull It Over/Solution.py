import re

def solution(line, part):
    total = 0

    enabled = True
    for command in re.findall(r"do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)", line):
        if command == 'do()':
            enabled = True
        elif command == "don't()":
            enabled = False
        elif part == 1 or (part == 2 and enabled):
            x, y = tuple([int(num) for num in re.findall(r"[0-9]{1,3}", command)])
            total += x * y

    return total


# # Result
with open("2024/Day 3 - Mull It Over/index.txt", 'r') as f:
    puzzleInput = f.read()

    print("Solution for part 1: ", solution(puzzleInput, 1))
    print("Solution for part 2: ", solution(puzzleInput, 2))