#!/usr/bin/env python3

file = open("input.txt")
loi = file.readlines()
file.close()

def Solution(inpt):
    total_overlap = 0
    for pair in inpt:
        pairs = pair.split(",")
        pairs = list(map(lambda s: s.split("-"), pairs))
        
        for i in range(0, len(pairs), 2):
            first = pairs[i]
            second = pairs[i + 1]

            if (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])) or (int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1])):
                total_overlap += 1

    return total_overlap


print(Solution(loi))



def Solution2(inpt):
    total_overlap = 0
    for pair in inpt:
        pairs = pair.split(",")
        pairs = list(map(lambda s: s.split("-"), pairs))

        for i in range(0, len(pairs), 2):
            first = pairs[i]
            second = pairs[i + 1]

            if (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[0])) or (int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[0])):
                total_overlap += 1

    return total_overlap


print(Solution2(loi))

