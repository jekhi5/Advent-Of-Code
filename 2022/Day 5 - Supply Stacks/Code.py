#!/usr/bin/env python3

file = open("input.txt")
loi = file.readlines()
file.close()

starting_matrix = [["T", "V", "J", "W", "N", "R", "M", "S"],
                   ["V", "C", "P", "Q", "J", "D", "W", "B"],
                   ["P", "R", "D", "H", "F", "J", "B"],
                   ["D", "N", "M", "B", "P", "R", "F"],
                   ["B", "T", "P", "R", "V", "H"],
                   ["T", "P", "B", "C"],
                   ["L", "P", "R", "J", "B"],
                   ["W", "B", "Z", "T", "L", "S", "C", "N"],
                   ["G", "S", "L"]]


def Solution(inpt):
    for line in inpt:
        split = line.split(" ")
        amt = int(split[1])
        start = int(split[3]) - 1
        end = int(split[5]) - 1

        for i in range(amt):
            change = starting_matrix[start].pop(0)
            starting_matrix[end].insert(0, change)

    result = ""
    for l in starting_matrix:
        result = result + l.pop(0)

    return result

print(Solution(loi))

starting_matrix = [["T", "V", "J", "W", "N", "R", "M", "S"],
                   ["V", "C", "P", "Q", "J", "D", "W", "B"],
                   ["P", "R", "D", "H", "F", "J", "B"],
                   ["D", "N", "M", "B", "P", "R", "F"],
                   ["B", "T", "P", "R", "V", "H"],
                   ["T", "P", "B", "C"],
                   ["L", "P", "R", "J", "B"],
                   ["W", "B", "Z", "T", "L", "S", "C", "N"],
                   ["G", "S", "L"]]

def Solution2(inpt):
    
    for line in inpt:
        split = line.split(" ")
        amt = int(split[1])
        start = int(split[3]) - 1
        end = int(split[5]) - 1

        for i in range(amt):
            change = starting_matrix[start].pop(0)
            starting_matrix[end].insert(i, change)

    result = ""
    for l in starting_matrix:
        result = result + l.pop(0)

    return result


print(Solution2(loi))
