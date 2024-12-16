#!/usr/bin/env python3

file = open("input.txt")
loi = file.read()
file.close()

def are_distinct(l):
    temp = set()

    for elem in l:
        temp.add(elem)

    return len(l) == len(temp)

def Solution(inpt):
    index = 0
    recent_four = []
    for char in inpt:
        if len(recent_four) > 3 and are_distinct(recent_four):
            return index
        elif len(recent_four) < 4:
            recent_four.append(char)
        else:
            recent_four.append(char)
            del recent_four[0]
        index += 1



print(Solution(loi))


def Solution2(inpt):
    index = 0
    recent_four = []
    for char in inpt:
        if len(recent_four) > 13 and are_distinct(recent_four):
            return index
        elif len(recent_four) < 14:
            recent_four.append(char)
        else:
            recent_four.append(char)
            del recent_four[0]
        
        index += 1

print(Solution2(loi))
