# This "solution" is horrible. The runtime for part two is
# horribly high for the input. It took over 13 hours to
# complete after each branch was threaded. I can't seem to think
# of the DP solution, but I'll be honest in that I haven't tried very hard


import threading

input = open(
    "/Users/jacobkline/Documents/Coding/Advent-Of-Code/2023/Day 5 - If You Give A Seed A Fertilizer/input.txt"
)
linesOfPuzzleInput = input.read()
input.close()


# Is the given character a number?
def isNumber(char):
    return ord(char) >= ORDINAL_ZERO and ord(char) <= ORDINAL_NINE


# Is the given number between the upper and lower bound
def isWithinRange(token, lowerBound, upperBound):
    return token >= lowerBound and token <= upperBound


linesOfPuzzleInput = linesOfPuzzleInput.split(":")
linesOfPuzzleInput[1] = linesOfPuzzleInput[1].split()

ORDINAL_ZERO = 48
ORDINAL_NINE = 57
DESTINATION_INDEX = 0
SOURCE_INDEX = 1
RANGE_LENGTH_INDEX = 2

# --------------- INPUT PARSING ---------------

seedNums = [
    int(token)
    for token in linesOfPuzzleInput[1]
    if all(list(map(isNumber, list(token))))
]

maps = []

for i in range(2, len(linesOfPuzzleInput)):
    curChunk = linesOfPuzzleInput[i]
    splitChunk = list(map(lambda c: c.split(), curChunk.split("\n")))
    explodedChunk = list(map(lambda lst: list(map(list, lst)), splitChunk))
    allAreNumbers = list(
        map(
            lambda listOfCharLists: len(listOfCharLists) > 0
            and all(
                list(
                    map(
                        lambda listOfChars: all(list(map(isNumber, listOfChars))),
                        listOfCharLists,
                    )
                )
            ),
            explodedChunk,
        )
    )

    maps.append(
        [
            list(map(int, splitChunk[j]))
            for j in range(len(splitChunk))
            if len(splitChunk[j]) == 3 and allAreNumbers[j] == True
        ]
    )

# ------------- END INPUT PARSING -------------


def partOneSolution():
    locationNumbers = []
    for seedNumber in seedNums:
        curNum = seedNumber
        for map in maps:
            for mapLine in map:
                if isWithinRange(
                    curNum,
                    mapLine[SOURCE_INDEX],
                    mapLine[SOURCE_INDEX] + mapLine[RANGE_LENGTH_INDEX],
                ):
                    curNum = mapLine[DESTINATION_INDEX] + abs(
                        mapLine[SOURCE_INDEX] - curNum
                    )
                    break

        locationNumbers.append(curNum)
        
    return min(locationNumbers)


def partTwoSoCalledSolutionHelper(seedNumber, seedNumberRange):
    minLocationNumbers = float("inf")

    curSeed = seedNumber

    while curSeed <= seedNumber + seedNumberRange:
        curNum = curSeed
        for map in maps:
            for mapLine in map:
                if isWithinRange(
                    curNum,
                    mapLine[SOURCE_INDEX],
                    mapLine[SOURCE_INDEX] + mapLine[RANGE_LENGTH_INDEX],
                ):
                    curNum = mapLine[DESTINATION_INDEX] + abs(
                        mapLine[SOURCE_INDEX] - curNum
                    )
                    break

        minLocationNumbers = min(curNum, minLocationNumbers)
        curSeed += 1

    print(minLocationNumbers, " ")


def partTwoSoCalledSolution():
    seedPairings = []

    for i in range(len(seedNums)):
        if i % 2 == 0:
            seed = seedNums[i]
            range = seedNums[i + 1]
            seedPairings.append([seed, range])

    for pairing in seedPairings:
        thread = threading.Thread(
            target=partTwoSoCalledSolutionHelper, args=(pairing[0], pairing[1])
        )
        thread.start()


print(partOneSolution())
# partTwoSoCalledSolutionHelper()
