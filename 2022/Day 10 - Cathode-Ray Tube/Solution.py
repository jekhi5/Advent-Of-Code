#!/usr/bin/env python3

file = open("input.txt")
loi = file.readlines()

def parse(inpt):
    result = []
    for elem in inpt:
        if " " in elem:
            result.append((elem[:elem.find(" ")], int(elem[elem.find(" ") + 1:])))
        else:
            result.append(elem)

    return result



loi = parse(loi)

file.close()

def update(cycle, x):
    if (cycle == 20 or (cycle - 20) % 40 == 0) and cycle <= 220:
        return x * cycle
        
    return 0

def render(x, cur_row):
    if x - 1 == cur_row or x == cur_row or x + 1 == cur_row:
        print("#", end="")
    else:
        print(".", end="")
    
    if cur_row == 39:
        print()

def Solution(inpt):

    cycle = 0
    total_strength = 0
    x = 1
    cur_row = 0
    for line in inpt:
            
        cycle += 1
        render(x, cur_row)
        if cur_row == 39:
            cur_row = 0
        else:
            cur_row += 1
        total_strength += update(cycle, x)
        
        if line[0] == "addx": 
            cycle += 1
            render(x, cur_row)
            if cur_row == 39:
                cur_row = 0
            else:
                cur_row += 1
            total_strength += update(cycle, x)
            x += line[1]
        
    print()
    return total_strength

print(Solution(loi))
