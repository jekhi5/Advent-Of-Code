# https://adventofcode.com/2023/day/1
# Runtime: O(n)

digitMap = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

ORDINALZERO = 48
ORDINALNINE = 57



# Attempts to find any spelled out digits within a given string.
# The digits can be found the in map of digits about^^
# The _reversed_ argument is a boolean identifying if the string was
# backwards and the digits located within them will also be reversed

# Returns a tuple containing either:
# - if a digit was found: (lowest digit found in substring, substring from index 0 to index of found digit)
# - if no digit was found: (None, '')
def findDigit(string, isReversed):
    for digit in digitMap:
        if digit in string and not isReversed:
            return (digit, string[0 : string.index(digit) + 1])
        elif digit[::-1] in string and isReversed:
            return (digit, string[0 : string.index(digit[::-1]) + 1])

    return (None, "")


# The solution function. Takes in the line as input along with a
# boolean value representing if the given line is reversed or not
# Outputs the first digit it finds in the string (reversed or not)
def calibrate(line, isReversed):
    # Iterate over each character
    for i in range(len(line)):
        curChar = line[i]

        # If the current character is a numerical digit or we are on the last
        # character of the line, then check to see if there are any spelled-out
        # digits that exist prior
        if (ord(curChar) >= ORDINALZERO and ord(curChar) <= ORDINALNINE) or i == len(
            line
        ) - 1:
            spelledOutDigit = ""
            preDigitSubstring = line[0:i + 1]

            # We save time by ensuring that the substring representing
            # the characters that come before the earliest number we've
            # found in the string so far is at least 3 characters long
            # because there are no numbers spelled with fewer letters
            while len(preDigitSubstring) > 2 and spelledOutDigit is not None:
                newDigit, preDigitSubstring = findDigit(preDigitSubstring, isReversed)
                if newDigit is not None:
                    spelledOutDigit = newDigit

            # If we didn't find a spelled out digit prior to the numeric, then
            # just use the numeric
            if (spelledOutDigit == None or spelledOutDigit == "") and (
                ord(curChar) >= ORDINALZERO and ord(curChar) <= ORDINALNINE
            ):
                return int(curChar)
            elif spelledOutDigit != None and spelledOutDigit != "":
                return digitMap[spelledOutDigit]


def main(lines):
    total = 0

    for line in lines:
        # Get the first digit by finding the first digit in the original string
        firstDigit = calibrate(line, False)

        # Get the second digit by finding the first digit in the reversed string
        secondDigit = calibrate(line[::-1], True)

        # If no numbers were found in the string, continue
        if firstDigit == None and secondDigit == None:
            continue

        # Combine them to create a two-digit number and add that to the total
        total += int(str(firstDigit) + str(secondDigit))

    return total


# # Result
file = open(
    "/Users/jacobkline/Documents/Coding/Advent-Of-Code/2023/Day 1 - Trebuchet?!/input.txt"
)
linesOfPuzzleInput = file.readlines()
file.close()

print("Solution: ", main(linesOfPuzzleInput))


# Tests
print(main([""]) == 0)
print(main(["1"]) == 11)
print(main(["13"]) == 13)
print(main(["178"]) == 18)

print(main(["abc"]) == 0)
print(main(["three"]) == 33)
print(main(["threefive"]) == 35)
print(main(["threefivesix"]) == 36)
print(main(["xyfdsafdzthreegasdfhdfiveasdffdssix"]) == 36)

print(main(["9andthreeand8"]) == 98)
print(main(["andthreeand89"]) == 39)
print(main(["xyfdsafd3zthreegasd4fhdfivea9sdffdssix"]) == 36)

print(main(["eightone2ninethreetwo"]) == 82)
