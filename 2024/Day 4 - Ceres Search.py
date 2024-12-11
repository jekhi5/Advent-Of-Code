import numpy as np

def findCrossedMasCount(textBlock):
    if (textBlock.shape != (3, 3)):
        return 0
    
    crossOne = ''.join([textBlock[idx][idx] for idx in range(3)])
    crossTwo = ''.join([textBlock[idx][2 - idx] for idx in range(3)])

    return sum(list(map(lambda word: 1 if word == 'MAS' or word == 'SAM' else 0, [crossOne, crossTwo]))) == 2

def findXmasCount(textBlock, row, col):
    left = None if col < 3 else list(reversed(textBlock[row, :4]))
    upLeft = None if row < 3 or col < 3 else [textBlock[row - idx][col - idx] for idx in range(4)]
    up = None if row < 3 else list(reversed(textBlock[:4, col]))
    upRight = None if row < 3 or textBlock.shape[1] - 1 - col < 3 else [textBlock[row - idx][col + idx] for idx in range(4)]
    right = None if textBlock.shape[1] - 1 - col < 3 else textBlock[row, col:]
    downRight = None if textBlock.shape[1] - 1 - col < 3 or textBlock.shape[0] - 1 - row < 3 else [textBlock[row + idx][col + idx] for idx in range(4)]
    down = None if textBlock.shape[0] - 1 - row < 3 else textBlock[row:, col]
    downLeft = None if col < 3 or textBlock.shape[0] - 1 - row < 3 else [textBlock[row + idx][col - idx] for idx in range(4)]

    return sum(list(map(lambda word: 1 if (''.join(word) == 'XMAS' if word is not None else False) else 0, [left, right, up, down, upLeft, upRight, downRight, downLeft])))
    


def solution(puzzle, part):
    puzzle = np.array(list((map(lambda line: list(line), puzzle.split('\n')))))
    xmasCount = 0

    for row in range(puzzle.shape[0]):
        for col in range(puzzle.shape[1]):
            if (part == 1):
                upRowIdx = max(0, row - 3)
                downRowIdx = min(puzzle.shape[0] + 1, row + 4)
                leftColIdx = max(0, col - 3)
                rightColIdx = min(puzzle.shape[1] + 1, col + 4)

                textBlock = np.array(puzzle[upRowIdx:downRowIdx, leftColIdx:rightColIdx])

                localRow = 3 if upRowIdx == row - 3 else row
                localCol = 3 if leftColIdx == col - 3 else col
                xmasCount += findXmasCount(textBlock, localRow, localCol)
            else:
                upRowIdx = row - 1
                downRowIdx = row + 2
                leftColIdx = col - 1
                rightColIdx = col + 2

                if upRowIdx < 0 or \
                   downRowIdx > puzzle.shape[0] + 1 or \
                   leftColIdx < 0 or \
                   rightColIdx > puzzle.shape[1] + 1: 
                    continue

                textBlock = np.array(puzzle[upRowIdx:downRowIdx, leftColIdx:rightColIdx])
                xmasCount += findCrossedMasCount(textBlock)
                

    
    return xmasCount


# # Result
with open("2024/inputs/4.txt", 'r') as f:
    puzzleInput = f.read()

    print("Solution for part 1: ", solution(puzzleInput, 1))
    print("Solution for part 2: ", solution(puzzleInput, 2))