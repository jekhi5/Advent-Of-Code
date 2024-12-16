#!/usr/bin/env python3

file = open("input.txt")
loi = file.readlines()
temp = []
for row in loi:
    new_row = list(row)
    for i in range(len(new_row)):
        if new_row[i] == "\n":
            continue
        new_row[i] = int(new_row[i])

    if "\n" in new_row: new_row.remove("\n")
    temp.append(new_row)

loi = temp

file.close()

def take_pass(inpt, result, index_of_left):

    for row in range(len(inpt)):
        cur_max = 0
        index_of_max = 0
        for col in range(len(inpt[row])):
            
            cur_height = inpt[row][col]

            # We're on the edge and that tree is visible
            if col == 0: 
                result[row][col][index_of_left] = (True, 0, (row, col), inpt[row][col])
                cur_max = inpt[row][col]
                index_of_max = 0
            elif cur_height > cur_max:
                result[row][col][index_of_left] = (True, col, (row, col), inpt[row][col])
                cur_max = inpt[row][col]
                index_of_max = col
            else:

                # Determine how many trees can be seen from this location if it cannot be seen from the edge
                
                count = 0
                for i in range(col - 1, index_of_max - 1, -1):
                    count += 1
                    if inpt[row][i] >= cur_height:
                        break

                result[row][col][index_of_left] = (False, count, (row, col), inpt[row][col])
                if cur_height == cur_max:
                    index_of_max = col
     


def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    #print("!!!!!")

def Solution(inpt):
    # Every elem in result is a list of 4 representing if it's visible from left, bottom, right, up
    result = [ [ [False] * 4 for i in range(len(inpt[0]))] for j in range(len(inpt))]
    
    for i in range(4):
        take_pass(inpt, result, i)
        rotate90Clockwise(inpt)
        rotate90Clockwise(result)
    
    count_of_visible = 0
    best_scenic_score = -1
    for row in result:
        for col in row:
            if col[0][0] or col[1][0] or col[2][0] or col[3][0]:
                count_of_visible += 1
            
            cur_score = col[0][1] * col[1][1] * col[2][1] * col[3][1]

            best_scenic_score = max(best_scenic_score, cur_score)

    
    return (count_of_visible, best_scenic_score)

result = Solution(loi)

print(result[0])
print(result[1])


