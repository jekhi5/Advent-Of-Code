# https://adventofcode.com/2023/day/11

input = open(
    "/Users/jacobkline/Documents/Coding/Advent-Of-Code/2023/Day 11 - Cosmic Expansion/input.txt"
)
lines = input.readlines()
input.close()

def findTotalPerms(springMap, nums):
    pass


def solution(input):
    total = 0
    for line in input:
        springMap = lines.split(" ")[0]
        nums = lines.split(" ")[1].split(",")

        total += findTotalPerms(springMap, nums)

    return total

print(solution(lines))