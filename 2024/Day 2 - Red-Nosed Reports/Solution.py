def checkSafety(nums, allowSkips):
    increasing = nums[0] - nums[1] < 0
    decreasing = nums[0] - nums[1] > 0
    prevNum = nums[0]
    for num in nums[1:]:
        if not (
            abs(prevNum - num) < 4
            and abs(prevNum - num) > 0
            and (
                (increasing and prevNum - num < 0) or (decreasing and prevNum - num > 0)
            )
        ):
            if allowSkips:
                skipOptions = [
                    [*nums[0:start], *nums[start + 1 :]]
                    for start in range(1, len(nums))
                ]
                skipOptions.append(nums[1:])
                return any(checkSafety(option, False) for option in skipOptions)

            return False

        prevNum = num

    return True


def solution(lines, part):
    totalSafeReports = 0

    for line in lines:
        totalSafeReports += (
            1
            if checkSafety(
                list(map(lambda numStr: int(numStr), line.split(" "))), part == 2
            )
            else 0
        )

    return totalSafeReports


# # Result
file = open("2024/Day 2 - Red-Nosed Reports/index.txt")
linesOfPuzzleInput = file.readlines()
file.close()

print("Solution for part 1: ", solution(linesOfPuzzleInput, 1))
print("Solution for part 2: ", solution(linesOfPuzzleInput, 2))
