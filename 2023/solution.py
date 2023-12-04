from pydoc import stripid


input = open("/Users/i41377/Desktop/input.txt")
linesOfInput = input.readlines()
input.close()

# total = 0

# for card in linesOfInput:
#     cardNums = list(filter(lambda str: len(str) > 0, (card[card.index(":") + 2:card.index("|") - 1].split(" "))))
#     yourNums = list(map(lambda str: str.rstrip(), list(filter(lambda str: len(str) > 0, (card[card.index("|") + 2:].split(" "))))))

#     winningPoints = 0

#     for num in yourNums:
#         if num in cardNums: 
#             if winningPoints == 0: winningPoints = 1
#             else: winningPoints *= 2

#     total += winningPoints

# print(total)

# card to tuple containing a tuple of (list of spawned indeces, number of times this card has spawned)
storedCards = {}

for curIndex in range(len(linesOfInput)):

    curCard = linesOfInput[curIndex]

    cardNums, yourNums = None, None

    if curCard in storedCards:
        for spawnedCardIndex in storedCards[curCard]["listOfSpwanedIndeces"]:
            storedCards[linesOfInput[spawnedCardIndex]]["countOfThisCardInLot"] += storedCards[curCard]["countOfThisCardInLot"]
    else:
        cardNums = list(filter(lambda str: len(str) > 0, (curCard[curCard.index(":") + 2:curCard.index("|") - 1].split(" "))))
        yourNums = list(map(lambda str: str.rstrip(), list(filter(lambda str: len(str) > 0, (curCard[curCard.index("|") + 2:].split(" "))))))

    numberOfWinningNumbers = 0

    for num in yourNums:
        if num in cardNums: 
            numberOfWinningNumbers += 1
    
    storedCards[curCard] = {
        "listOfSpawnedIndeces": [i for i in range(curIndex + 1, curIndex + numberOfWinningNumbers + 1)],
        "countOfThisCardInLot": 1
        }
    
# iterate through one more time and update all keys

total = 0

for curIndex in range(len(linesOfInput)):
    listOfSpawnedCardsIndeces = storedCards[linesOfInput[curIndex]]["listOfSpawnedIndeces"]
    amtOfCurCard = storedCards[linesOfInput[curIndex]]["countOfThisCardInLot"]

    for index in listOfSpawnedCardsIndeces:
        storedCards[linesOfInput[index]]["countOfThisCardInLot"] += amtOfCurCard
    
    total += amtOfCurCard


print(total)