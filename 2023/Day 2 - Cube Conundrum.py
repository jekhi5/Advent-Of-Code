file = open(
    "/Users/jacobkline/Documents/Coding/Advent-Of-Code/2023/Day 2 - Cube Conundrum/input.txt"
)
linesOfPuzzleInput = file.readlines()
file.close()


def solution(isPartOne):
    total = 0

    for round in linesOfPuzzleInput:
        id = round[round.index(" ") + 1 : round.index(":")]
        truncatedRound = round[round.index(":") + 1 :]

        handfuls = truncatedRound.split(";")

        handfulMaximums = {}

        for handful in handfuls:
            separateColors = handful.split(",")
            for singleColorSelection in separateColors:
                amountPicked = singleColorSelection[
                    singleColorSelection.index(" ")
                    + 1 : singleColorSelection[
                        singleColorSelection.index(" ") + 1 :
                    ].index(" ")
                    + singleColorSelection.index(" ")
                    + 1
                ]
                colorName = singleColorSelection[
                    singleColorSelection[singleColorSelection.index(" ") + 1 :].index(
                        " "
                    )
                    + singleColorSelection.index(" ")
                    + 2 : len(singleColorSelection)
                ]

                if "\n" in colorName:
                    colorName = colorName[0 : len(colorName) - 1]
                # print("colorPick:" + colorPick)
                # print("amt:" + amt)
                # print("colorName:" + colorName)
                if colorName in handfulMaximums:
                    handfulMaximums[colorName] = max(
                        int(amountPicked), handfulMaximums[colorName]
                    )
                else:
                    handfulMaximums[colorName] = int(amountPicked)

        if isPartOne:
            if (
                handfulMaximums["red"] <= 12
                and handfulMaximums["green"] <= 13
                and handfulMaximums["blue"] <= 14
            ):
                total += int(id)
        else:
            redTotal = 0
            greenTotal = 0
            blueTotal = 0

            if "red" in handfulMaximums:
                redTotal = handfulMaximums["red"]
            if "green" in handfulMaximums:
                greenTotal = handfulMaximums["green"]
            if "blue" in handfulMaximums:
                blueTotal = handfulMaximums["blue"]

            power = redTotal * blueTotal * greenTotal
            total += power

    return total


print(solution(False))
