# https://adventofcode.com/2023/day/4
# O(n)

input = open("/Users/i41377/Desktop/input.txt")
linesOfInput = input.readlines()
input.close()


def solution(isPartOne):

    # card to tuple containing a tuple of (list of spawned indeces, number of times this card has spawned)
    storedCards = []

    # Load up the stored cards dictionary
    for curIndex in range(len(linesOfInput)):

        # The current scratchoff card that we're working on
        curCard = linesOfInput[curIndex]

        # Store the values for the card numbers and our numbers. Kinda janky but that's how we have to parse the input data
        cardNums = list(filter(lambda str: len(str) > 0, (curCard[curCard.index(":") + 2:curCard.index("|") - 1].split(" "))))
        yourNums = list(map(lambda str: str.rstrip(), list(filter(lambda str: len(str) > 0, (curCard[curCard.index("|") + 2:].split(" "))))))

        # Represents the total number of winning numbers
        numberOfWinningNumbers = 0
        totalPoints = 0

        # For each winning number, increment the total number of winning numbers for that card and also set/double the number of points for that card
        for num in yourNums:
            if num in cardNums: 
                numberOfWinningNumbers += 1
                if totalPoints == 0: totalPoints = 1
                else: totalPoints *= 2
        
        # Store that cards resulting data in the storedCards dictionary
        storedCards.append({
            # Represents which cards (represented by the index they appear in the input data) will be spawned by playing this card
            "listOfSpawnedIndeces": [i for i in range(curIndex + 1, curIndex + numberOfWinningNumbers + 1)],

            # Represents the total number of points this card is worth after totalling the winning numbers
            "totalPoints": totalPoints,

            # How many copies of this card have been generated in total by other cards
            "countOfThisCardInLot": 1
            })
        

    total = 0

    # Iterate one more time 
    for curCardData in storedCards:
        listOfSpawnedCardsIndeces = curCardData["listOfSpawnedIndeces"]
        

        # If we're in part one, just add up the total number of points
        if isPartOne: total += curCardData["totalPoints"]
        else:
            # For each card that is spawned because of the winning numbers of this card, 
            # increment the total number of copies of that card by the total number of this card
            amtOfCurCard = curCardData["countOfThisCardInLot"] 
            for index in listOfSpawnedCardsIndeces: storedCards[index]["countOfThisCardInLot"] += amtOfCurCard
            total += amtOfCurCard

    return total

print(solution(True))
print(solution(False))
