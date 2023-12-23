input = open("/Users/i41377/Desktop/input.txt")
maze = list(map(lambda str: list(map(lambda c: { "char": c, "pathLength": 0 } if c != "S" else { "char": c, "pathLength": 0 }, list(str.strip()))), input.readlines()))
input.close()

indexOfStart = None

for rowIndex in range(len(maze)):
    for colIndex in range(len(maze[rowIndex])):
        if maze[rowIndex][colIndex]["char"] == "S": indexOfStart = (rowIndex, colIndex); break
    
    if indexOfStart is not None: break


def DFS(maze, startingRow, startingCol, dir, isPartOne):
    
    queue = [maze[startingRow][startingCol]]
    prevLoc = { "pathLength": 0 }

    curRow = startingRow
    curCol = startingCol

    lowestRow = startingRow
    highestRow = startingRow

    lowestCol = startingCol
    highestCol = startingCol

    while len(queue) > 0:
        curLoc = queue.pop(0)
        curLoc["pathLength"] = prevLoc["pathLength"] + 1

        lowestRow = min(lowestRow, curRow)
        highestRow = max(highestRow, curRow)

        lowestCol = min(lowestCol, curCol)
        highestCol = max(highestCol, curCol)

        if curLoc["char"] == "S":
            if isPartOne: return int((curLoc["pathLength"] + 1) / 2)
            else: curLoc["char"] = "G"; break
        elif dir == "U":
            if curLoc["char"] == "|":
                curRow -= 1
                queue.append(maze[curRow][curCol])
                dir = "U"
            if curLoc["char"] == "F":
                curCol += 1
                queue.append(maze[curRow][curCol])
                dir = "R"
            if curLoc["char"] == "7":
                curCol -= 1
                queue.append(maze[curRow][curCol])
                dir = "L"
        elif dir == "D":
            if curLoc["char"] == "|":
                curRow += 1
                queue.append(maze[curRow][curCol])
                dir = "D"
            if curLoc["char"] == "L":
                curCol += 1
                queue.append(maze[curRow][curCol])
                dir = "R"
            if curLoc["char"] == "J":
                curCol -= 1
                queue.append(maze[curRow][curCol])
                dir = "L"
        elif dir == "R":
            if curLoc["char"] == "-":
                curCol += 1
                queue.append(maze[curRow][curCol])
                dir = "R"
            if curLoc["char"] == "7":
                curRow += 1
                queue.append(maze[curRow][curCol])
                dir = "D"
            if curLoc["char"] == "J":
                curRow -= 1
                queue.append(maze[curRow][curCol])
                dir = "U"
        elif dir == "L":
            if curLoc["char"] == "-":
                curCol -= 1
                queue.append(maze[curRow][curCol])
                dir = "L"
            if curLoc["char"] == "L":
                curRow -= 1
                queue.append(maze[curRow][curCol])
                dir = "U"
            if curLoc["char"] == "F":
                curRow += 1
                queue.append(maze[curRow][curCol])
                dir = "D"
        
        prevLoc = curLoc
    


    newMaze = [[col["char"] for col in row[lowestCol:highestCol + 1]] for row in maze[lowestRow:highestRow + 1]]

    totalBlanks = 0

    for row in newMaze:
        isInside = False
        countOfEmptySlots = 0
        for c in row:
            if c == "|" or c == "F" or c == "L":
                if isInside:
                    totalBlanks += countOfEmptySlots
                    countOfEmptySlots = 0
                    isInside = not isInside
                else:
                    isInside = not isInside
                    countOfEmptySlots = 0
                
            elif c == ".":
                countOfEmptySlots += 1
        
        print(list(map(lambda elem: elem, row)))
    
    return totalBlanks








curRow = indexOfStart[0]
curCol = indexOfStart[1]

# # Right
# if maze[curRow][curCol + 1]["char"] == "-" or maze[curRow][curCol + 1]["char"] == "J" or maze[curRow][curCol + 1]["char"] == "7":
#     print(DFS(maze, curRow, curCol + 1, "R", True))

# # Left
# elif maze[curRow][curCol - 1]["char"] == "-" or maze[curRow][curCol - 1]["char"] == "L" or maze[curRow][curCol - 1]["char"] == "F":
#     print(DFS(maze, curRow, curCol - 1, "L", True))

# # Down
# elif maze[curRow + 1][curCol]["char"] == "|" or maze[curRow + 1][curCol]["char"] == "L" or maze[curRow + 1][curCol]["char"] == "J":
#     print(DFS(maze, curRow + 1, curCol, "D", True))

# # Up
# elif maze[curRow - 1][curCol]["char"] == "|" or maze[curRow - 1][curCol]["char"] == "7" or maze[curRow - 1][curCol]["char"] == "F":
#     print(DFS(maze, curRow - 1, curCol, "U", True))

# ------------------------------------------

# Right
if maze[curRow][curCol + 1]["char"] == "-" or maze[curRow][curCol + 1]["char"] == "J" or maze[curRow][curCol + 1]["char"] == "7":
    print(DFS(maze, curRow, curCol + 1, "R", False))

# Left
elif maze[curRow][curCol - 1]["char"] == "-" or maze[curRow][curCol - 1]["char"] == "L" or maze[curRow][curCol - 1]["char"] == "F":
    print(DFS(maze, curRow, curCol - 1, "L", False))

# Down
elif maze[curRow + 1][curCol]["char"] == "|" or maze[curRow + 1][curCol]["char"] == "L" or maze[curRow + 1][curCol]["char"] == "J":
    print(DFS(maze, curRow + 1, curCol, "D", False))

# Up
elif maze[curRow - 1][curCol]["char"] == "|" or maze[curRow - 1][curCol]["char"] == "7" or maze[curRow - 1][curCol]["char"] == "F":
    print(DFS(maze, curRow - 1, curCol, "U", False))


