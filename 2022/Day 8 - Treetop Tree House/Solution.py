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
        for col in range(len(inpt[row])):
            
            cur_height = inpt[row][col]

            # We're on the edge and that tree is visible
            if col == 0: 
                result[row][col][index_of_left] = True
                cur_max = inpt[row][col]
            else:
                if cur_height > cur_max:
                    result[row][col][index_of_left] = True
                    cur_max = inpt[row][col]

def rotate90Clockwise(A):
    #for row in A:
        #print(row)

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
    result = [ [ [None] * 4 for i in range(len(inpt[0]))] for j in range(len(inpt))]
    
    for i in range(4):
        take_pass(inpt, result, i)
        #print("ROTATING INPUT")
        rotate90Clockwise(inpt)
        
        #for row in inpt:
            #print(row)
        
        #print("ROTATING RESULT")
        rotate90Clockwise(result)
        #for row in result:
           # print(row)
    
    count = 0
    for row in result:
        for col in row:
            if col[0] or col[1] or col[2] or col[3]:
                count += 1
    #print("!!!!!!!")
    rotate90Clockwise(result)
    return count

print(Solution(loi))


