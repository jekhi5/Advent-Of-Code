# https://adventofcode.com/2023/day/6
# O(nlog(n))

input = open("/Users/jacobkline/Coding/Advent-Of-Code/input.txt")
lines = input.readlines()
input.close()

def solution(isPartTwo):

    times, records = None, None

    # If it's part 2, we concatinate all times and records to a 
    # single number, for part one they remain separate
    if isPartTwo:
        times = [int(''.join(list(map(lambda str: str.strip(), lines[0].split(":")[1].split()))))]
        records = [int(''.join(list(map(lambda str: str.strip(), lines[1].split(":")[1].split()))))]
    else:    
        times = list(map(lambda str: int(str.strip()), lines[0].split(":")[1].split()))
        records = list(map(lambda str: int(str.strip()), lines[1].split(":")[1].split()))

    # We're multiplying, so base is 1 ot 0
    total = 1

    numberOfRaces = len(times)

    # Loop through each race and calculate the number of winning button-press times
    # O(nlog(n))
    for i in range(numberOfRaces):
        # The loop operates like a binary search
        # The target is the shortest amount of time you can hold the 
        # button while still beating the record


        time = times[i]
        record = records[i]

        upperBound = time
        lowerBound = 0

        buttonPressTime = 0
        distance = 0

        mostRecentSuccessfulButtonPressTime = 0
        shortestButtonPress = 0

        # O(log(n))
        while upperBound != lowerBound:
            buttonPressTime = lowerBound + int((upperBound - lowerBound) / 2)
            distance = buttonPressTime * (time - buttonPressTime)

            if distance > record: 
                mostRecentSuccessfulButtonPressTime = buttonPressTime
                if upperBound - lowerBound == 1: 
                    upperBound = lowerBound
                    shortestButtonPress = mostRecentSuccessfulButtonPressTime
                else: upperBound -= int((upperBound - lowerBound) / 2)
            elif distance <= record: 
                if upperBound - lowerBound == 1: 
                    lowerBound = upperBound
                    shortestButtonPress = mostRecentSuccessfulButtonPressTime
                else: lowerBound += int((upperBound - lowerBound) / 2)
        
        # The bell curve for winning times for button presses is uniform.
        # If the shortest amount of time you can press the button and still 
        # beat the record is 4 seconds, then the longest amount of time 
        # you can press the button while still beating the record is
        # the full time limit minus 4
        numberOfWaysToWin = (time - shortestButtonPress) - shortestButtonPress + 1
        total *= numberOfWaysToWin

    return total

print("Part one: ", solution(False))
print("Part two: ", solution(True))
