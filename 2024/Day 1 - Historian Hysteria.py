def solution(lines, part):
    listOne = []
    listTwo = []

    for line in lines:
        nums = line.split("   ")
        listOne.append(int(nums[0]))
        listTwo.append(int(nums[1]))

    if len(listOne) != len(listTwo):
        SyntaxError("Lists have different lengths!")

    listOne.sort()
    result = 0
    idx = 0

    if part == 1:
        listTwo.sort()

    for num in listOne:
        if part == 1:
            result += abs(num - listTwo[idx])
        elif part == 2:
            result += len([numTwo for numTwo in listTwo if numTwo == num]) * num
        else:
            ValueError("Problem part not valid")

        idx += 1

    return result


# # Result
file = open("2024/inputs/1.txt")
linesOfPuzzleInput = file.readlines()
file.close()

print("Solution for part 1: ", solution(linesOfPuzzleInput, 1))
print("Solution for part 2: ", solution(linesOfPuzzleInput, 2))
