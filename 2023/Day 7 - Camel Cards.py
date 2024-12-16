# https://adventofcode.com/2023/day/7

input = open("2023/Day 7 - Camel Cards/input.txt")
lines = input.readlines()
input.close()

puzzleDict = [
    {
        "hand": line.split(" ")[0],
        "bet": int(line.split(" ")[1].strip()),
    }
    for line in lines
]

orderOfCards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1"]


def placeInList(pastListOfHands, newHand):
    for i in range(len(pastListOfHands)):
        pastHand = pastListOfHands[i]
        for charIndex in range(0, 5):
            pastHandPlaceInHierarchy = orderOfCards.index(pastHand[charIndex])
            newHandPlaceInHierarchy = orderOfCards.index(newHand[charIndex])
            if pastHandPlaceInHierarchy > newHandPlaceInHierarchy:
                pastListOfHands.insert(i, newHand)
                return
            elif pastHandPlaceInHierarchy == newHandPlaceInHierarchy:
                continue
            else:
                break

    pastListOfHands.append(newHand)


ranks = {
    "five": [],
    "four": [],
    "fullHouse": [],
    "three": [],
    "twoPair": [],
    "pair": [],
    "high": [],
}

handToBetMap = {}

for player in puzzleDict:
    unsortedHand = player["hand"]
    sortedHand = "".join(sorted(unsortedHand, key=str.lower))
    bet = player["bet"]

    handToBetMap[unsortedHand] = bet

    firstChar = sortedHand[0]

    countOfChar = sortedHand.count(firstChar)
    if countOfChar == 5:
        placeInList(ranks["five"], unsortedHand)
    elif countOfChar == 4:
        placeInList(ranks["four"], unsortedHand)
    elif countOfChar == 3:
        nextChar = sortedHand[3]
        if sortedHand.count(nextChar) == 2:
            placeInList(ranks["fullHouse"], unsortedHand)
        else:
            placeInList(ranks["three"], unsortedHand)
    elif countOfChar == 2:
        nextChar = sortedHand[2]
        if sortedHand.count(nextChar) == 3:
            placeInList(ranks["fullHouse"], unsortedHand)
        elif sortedHand.count(nextChar) == 2:
            placeInList(ranks["twoPair"], unsortedHand)
        else:
            nextChar = sortedHand[4]
            if sortedHand.count(nextChar) == 2:
                placeInList(ranks["twoPair"], unsortedHand)
            else:
                placeInList(ranks["pair"], unsortedHand)
    elif countOfChar == 1:
        nextChar = sortedHand[1]
        if sortedHand.count(nextChar) == 4:
            placeInList(ranks["four"], unsortedHand)
        elif sortedHand.count(nextChar) == 3:
            placeInList(ranks["three"], unsortedHand)
        elif sortedHand.count(nextChar) == 2:
            nextChar = sortedHand[3]
            if sortedHand.count(nextChar) == 2:
                placeInList(ranks["twoPair"], unsortedHand)
            else:
                placeInList(ranks["pair"], unsortedHand)
        else:
            nextChar = sortedHand[2]
            if sortedHand.count(nextChar) == 3:
                placeInList(ranks["three"], unsortedHand)
            elif sortedHand.count(nextChar) == 2:
                placeInList(ranks["pair"], unsortedHand)
            else:
                nextChar = sortedHand[3]ּּּּּּּּּּּּּ
                if sortedHand.count(nextChar) == 2:
                    placeInList(ranks["pair"], unsortedHand)
                else:
                    placeInList(ranks["high"], unsortedHand)


print(ranks)

total = 0
currentRank = len(lines)
for key in ranks.keys():
    for hand in ranks[key]:
        total += handToBetMap[hand] * currentRank
        currentRank -= 1

print(total)
