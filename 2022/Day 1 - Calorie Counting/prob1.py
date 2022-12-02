#!/usr/bin/env python

def solution1(path):
    file = open(path)
    lines = file.readlines()
    file.close()

    maximum = 0
    cur_max = 0
    for line in lines:
        if line == "\n":
            maximum = max(maximum, cur_max)
            cur_max = 0
            continue
        else:
            num = int(line)
            cur_max += num

    return maximum


def solution2(path):
    file = open(path)
    lines = file.readlines()
    file.close()

    # Invariant: max1 >= max2 >= max3
    max1 = 0
    max2 = 0
    max3 = 0
    
    cur_max = 0
    for line in lines:
        if line == "\n":
            temp1 = max1
            temp2 = max2
            
            if cur_max > max1:
                max1 = cur_max
                max2 = temp1
                max3 = temp2
            elif cur_max > max2:
                max2 = cur_max
                max3 = temp2
            elif cur_max > max3:
                max3 = cur_max

            totals.append(cur_max)
            cur_max = 0
            continue
        else:
            num = int(line)
            cur_max += num

    return max1 + max2 + max3

print(solution1("input.txt"))

print(solution2("input.txt"))
