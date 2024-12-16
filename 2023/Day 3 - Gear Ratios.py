ORDINALZERO = 48
ORDINALNINE = 57


# Is the given character a number?
def isNumber(char):
    return ord(char) >= ORDINALZERO and ord(char) <= ORDINALNINE


# Is the given row and col within the bounds of the given schematic?
def isInBounds(schematic, row, col):
    return row >= 0 and row < len(schematic) and col >= 0 and col < len(schematic[row])


# Given the schematic and the coordinates for a digit in a number, returns a dictionary containing:
# - the entire number that was found
# - the row that the number is on
# - the starting column that the number is on
# - the ending column that the number is on
def findWholeNumber(schematic, curRow, curCol):
    startingCol = curCol

    earliestIndexOfNumber = -1
    lastIndexOfNumber = -1

    while isInBounds(schematic, curRow, curCol) and isNumber(schematic[curRow][curCol]):
        curCol -= 1

    earliestIndexOfNumber = curCol + 1

    curCol = startingCol
    while isInBounds(schematic, curRow, curCol) and isNumber(schematic[curRow][curCol]):
        curCol += 1

    lastIndexOfNumber = curCol - 1

    return {
        "number": int(
            "".join(schematic[curRow][earliestIndexOfNumber : lastIndexOfNumber + 1])
        ),
        "startingRow": curRow,
        "startingCol": earliestIndexOfNumber,
        "endingCol": lastIndexOfNumber,
    }


# Given the schematic and indecies of where a number is, turn that number into "."s
# Returns the schematic
def removeNumberFromSchematic(schematic, row, startingCol, endingCol):
    for i in range(startingCol, endingCol + 1):
        schematic[row][i] = "."

    return schematic


class GreaterThanTwoIdsForSingleGearError(Exception):
    pass


def solution(schematic, isPartTwo):
    total = 0

    for rowIndex in range(len(schematic)):
        for colIndex in range(len(schematic[rowIndex])):
            curValue = schematic[rowIndex][colIndex]

            isValidPart = False
            if isPartTwo:
                isValidPart = curValue == "*"
            else:
                isValidPart = (
                    curValue != "." and curValue != "\n" and not isNumber(curValue)
                )

            if isValidPart:

                def updateSchematic(schematic, rowChange, colChange, numberOfIdsFound):
                    if isPartTwo and numberOfIdsFound > 2:
                        raise

                    if isInBounds(
                        schematic, rowIndex + rowChange, colIndex + colChange
                    ) and isNumber(
                        schematic[rowIndex + rowChange][colIndex + colChange]
                    ):
                        numberMap = findWholeNumber(
                            schematic, rowIndex + rowChange, colIndex + colChange
                        )
                        removeNumberFromSchematic(
                            schematic,
                            numberMap["startingRow"],
                            numberMap["startingCol"],
                            numberMap["endingCol"],
                        )
                        return numberMap["number"]
                    else:
                        if isPartTwo:
                            return 1
                        else:
                            return 0

                numberOfIdsFound = 0
                numbersFound = []

                try:
                    numbersFound.append(
                        updateSchematic(linesOfPuzzleInput, -1, -1, numberOfIdsFound)
                    )
                    if isPartTwo and numbersFound[-1] > 1:
                        numberOfIdsFound += 1

                    numbersFound.append(
                        updateSchematic(linesOfPuzzleInput, -1, 0, numberOfIdsFound)
                    )
                    if isPartTwo and numbersFound[-1] > 1:
                        numberOfIdsFound += 1

                    numbersFound.append(
                        updateSchematic(linesOfPuzzleInput, -1, +1, numberOfIdsFound)
                    )
                    if isPartTwo and numbersFound[-1] > 1:
                        numberOfIdsFound += 1

                    numbersFound.append(
                        updateSchematic(linesOfPuzzleInput, 0, -1, numberOfIdsFound)
                    )
                    if isPartTwo and numbersFound[-1] > 1:
                        numberOfIdsFound += 1

                    # The location of the part has a 0, 0 change so no point in checking
                    numbersFound.append(
                        updateSchematic(linesOfPuzzleInput, 0, +1, numberOfIdsFound)
                    )
                    if isPartTwo and numbersFound[-1] > 1:
                        numberOfIdsFound += 1

                    numbersFound.append(
                        updateSchematic(linesOfPuzzleInput, +1, -1, numberOfIdsFound)
                    )
                    if isPartTwo and numbersFound[-1] > 1:
                        numberOfIdsFound += 1

                    numbersFound.append(
                        updateSchematic(linesOfPuzzleInput, +1, 0, numberOfIdsFound)
                    )
                    if isPartTwo and numbersFound[-1] > 1:
                        numberOfIdsFound += 1

                    numbersFound.append(
                        updateSchematic(linesOfPuzzleInput, +1, +1, numberOfIdsFound)
                    )
                    if isPartTwo and numbersFound[-1] > 1:
                        numberOfIdsFound += 1

                    result = 0
                    if isPartTwo and numberOfIdsFound == 2:
                        result = 1
                        for num in numbersFound:
                            result *= num
                    elif not isPartTwo:
                        result = sum(numbersFound)

                    total += result
                except GreaterThanTwoIdsForSingleGearError:
                    continue

    return total


file = open(
    "/Users/jacobkline/Documents/Coding/Advent-Of-Code/2023/Day 3 - Gear Ratios/index.txt"
)
linesOfPuzzleInput = file.readlines()
linesOfPuzzleInput = [[char for char in l] for l in linesOfPuzzleInput]
file.close()
print(solution(linesOfPuzzleInput, False))

file = open(
    "/Users/jacobkline/Documents/Coding/Advent-Of-Code/2023/Day 3 - Gear Ratios/index.txt"
)
linesOfPuzzleInput = file.readlines()
linesOfPuzzleInput = [[char for char in l] for l in linesOfPuzzleInput]
file.close()
print(solution(linesOfPuzzleInput, True))


# Testing:

print(
    solution(
        [
            [char for char in l]
            for l in [
                "467..114..",
                "...*......",
                "..35..633.",
                "......#...",
                "617*......",
                ".....+.58.",
                "..592.....",
                "......755.",
                "...$.*....",
                ".664.598..",
            ]
        ],
        False,
    )
    == 4361
)

print(
    solution(
        [
            [char for char in l]
            for l in [
                "467..114..",
                "...*......",
                "..35..633.",
                "......#...",
                "617*......",
                ".....+.58.",
                "..592.....",
                "......755.",
                "...$.*....",
                ".664.598..",
            ]
        ],
        True,
    )
    == 467835
)
