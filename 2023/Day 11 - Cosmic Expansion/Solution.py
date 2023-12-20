# https://adventofcode.com/2023/day/11

input = open(
    "/Users/jacobkline/Documents/Coding/Advent-Of-Code/2023/Day 11 - Cosmic Expansion/input.txt"
)
lines = input.readlines()
input.close()

newHorizontalGalaxy = []

for line in lines:
    if not "#" in line:
        newHorizontalGalaxy.append(["+" for _ in range(len(line))])
    else:
        newHorizontalGalaxy.append(line)

rotatedGraph = list(zip(*newHorizontalGalaxy[::-1]))
expandedGalaxy = []

for line in rotatedGraph:
    if not "#" in line:
        expandedGalaxy.append(["+" for _ in range(len(line))])
    else:
        expandedGalaxy.append(line)

expandedGalaxy = list(zip(*expandedGalaxy[::-1]))
expandedGalaxy = list(reversed(list(map(lambda l: list(reversed(l)), expandedGalaxy))))

listOfStars = []

for row in range(len(expandedGalaxy)):
    for col in range(len(expandedGalaxy[row])):
        if expandedGalaxy[row][col] == "#":
            listOfStars.append((row, col))


def solution(listOfStars, galaxy, MULTIPLE):
    total = 0

    for i in range(len(listOfStars)):
        fromStar = listOfStars[i]

        for j in range(i + 1, len(listOfStars)):
            toStar = listOfStars[j]

            fromY = fromStar[0]
            toY = toStar[0]

            multiplesToAdd = 0
            subRows = galaxy[fromY : toY + 1]

            for row in subRows:
                multiplesToAdd += 1 if row.count("+") == len(row) else 0

            rotated = list(zip(*subRows[::-1]))
            for row in rotated[
                min(fromStar[1], toStar[1]) : max(fromStar[1], toStar[1]) + 1
            ]:
                multiplesToAdd += 1 if row.count("+") == len(row) else 0

            distance = (
                abs(fromStar[0] - toStar[0])
                + abs(fromStar[1] - toStar[1])
                - multiplesToAdd
                + (MULTIPLE * multiplesToAdd)
            )

            total += distance

    return total


print("Part 1: ", solution(listOfStars, expandedGalaxy, 2))
print("Part 2: ", solution(listOfStars, expandedGalaxy, 1000000))
