# https://adventofcode.com/2023/day/9

input = open("/Users/i41377/Desktop/input.txt")
lines = input.readlines()
input.close()

def solution(isPartOne):

    total = 0
    significantIndex = -1 if isPartOne else 0

    for line in lines:
        curLine = list(map(int, line.split()))
        significantNumInLines = [curLine[significantIndex]]

        isAllZero = False

        while not isAllZero:
            newLine = []
            isAllZero = True

            for i in range(len(curLine) - 1):
                firstNum = curLine[i]
                secondNum = curLine[i + 1]

                newNum = secondNum - firstNum
                isAllZero = isAllZero and newNum == 0

                newLine.append(secondNum - firstNum)
            
            curLine = newLine
            significantNumInLines.insert(0, newLine[significantIndex])

        if isPartOne:
            total += sum(significantNumInLines)
        else:
            numToSubtract = significantNumInLines[0]

            for i in range(1, len(significantNumInLines)):
                cur = significantNumInLines[i]
                numToSubtract = cur - numToSubtract
            
            total += numToSubtract


    return total

print("Part 1: ", solution(True))
print("Part 2: ", solution(False))
