def solution(lines, part=1):
    curNum = 50
    count = 0
    for entry in lines:
        change = -int(entry[1:]) if entry[0] == "L" else int(entry[1:])
        newNumUnbounded = curNum + change
        nextNum = (
            newNumUnbounded
            if 0 <= newNumUnbounded and newNumUnbounded < 100
            else newNumUnbounded % 100
        )
        if part == 1:
            count += 1 if nextNum == 0 else 0
        if part == 2:
            if newNumUnbounded <= 0 or newNumUnbounded >= 100:
                passedZero = int(abs(newNumUnbounded / 100)) + 1
                count += passedZero if change < 0 and curNum != 0 else passedZero - 1

        curNum = nextNum

    return count


file = open("2025/inputs/1.txt")
linesOfPuzzleInput = file.readlines()
file.close()

print("Solution for part 1: ", solution(linesOfPuzzleInput, 1))
print("Solution for part 2: ", solution(linesOfPuzzleInput, 2))
