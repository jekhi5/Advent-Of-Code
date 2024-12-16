#!/usr/bin/env python3
import math, sys, copy

loi = None
with open("input.txt") as file:
    loi = file.readlines()
    
coords = []
min_x = sys.maxsize

max_x = -sys.maxsize
max_y = -sys.maxsize
for line in loi:
    cur = []
    coordinates = line.split(" -> ")
    for point in coordinates:
        x = int(point.split(",")[0])
        y = int(point.split(",")[1])
        
        min_x = min(min_x, x)

        max_x = max(max_x, x)
        max_y = max(max_y, y)

        coord = (x, y)
        cur.append(coord)

    coords.append(cur)



cave_map = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y + 1)]

for lo_coords in coords:
    for i in range(len(lo_coords) - 1):
        start = lo_coords[i]
        end = lo_coords[i + 1]
        
        is_horiz = start[1] == end[1]

        if is_horiz:
            temp_start = min(start, end, key=lambda x: x[0])
            end = end if temp_start == start else start
            start = temp_start

            scaled_starting_x = start[0] - min_x

            # Make the line along the x axis
            for j in range(scaled_starting_x, scaled_starting_x + (end[0] - start[0]) + 1):
                cave_map[start[1]][j] = "#"
        else:
            temp_start = min(start, end, key=lambda x: x[1])
            end = end if temp_start == start else start
            start = temp_start

            # Make the line along the y axis
            for j in range(start[1], start[1] + (end[1] - start[1]) + 1):
                cave_map[j][start[0] - min_x] = "#"


rested = True
count = 0
while rested:
    y = 0
    x = 500 - min_x
    
    try:
        while cave_map[y + 1][x] == "." or cave_map[y + 1][x - 1] == "." or cave_map[y + 1][x + 1] == ".":
            if cave_map[y + 1][x] == ".":
                pass
            elif cave_map[y + 1][x - 1] == ".":
                x -= 1
            elif cave_map[y + 1][x + 1] == ".":
                x += 1
            
            y += 1
        
        cave_map[y][x] = "o"
        count += 1
        rested = True
    except IndexError:
        rested = False


print("RESULT 1: ", count)
part_2_count = count

cave_map.append(["." for _ in range(len(cave_map[0]))])
cave_map.append(["#" for _ in range(len(cave_map[0]))])

source_x = 500 - min_x
source = cave_map[0][source_x]
while source == ".":
    y = 0
    x = source_x
    
    down = cave_map[y + 1][x]
    down_left = cave_map[y + 1][x - 1]
    down_right = cave_map[y + 1][x + 1]
    
    while down == "." or down_left == "." or down_right == ".":
        if cave_map[y + 1][x] == ".":
            pass
        elif x != 0 and cave_map[y + 1][x - 1] == ".":
            x -= 1
        elif x != len(cave_map[0]) - 1 and cave_map[y + 1][x + 1] == ".":
            x += 1
        

        y += 1
        
        if x == 0:
            # Extend the cave to the left
            for row in cave_map:
                row.insert(0, ".")

            # Be sure to maintain the floor
            cave_map[-1][0] = "#"

            # We just extended the cave to the left so the source and the x is now one higher than it was before
            source_x += 1
            x += 1
        
        if x == len(cave_map[0]) - 1:
            # Extend the cave to the right
            for row in cave_map:
                row.append(".")
            # Be sure to maintain the floor
            cave_map[-1][-1] = "#"

        down = cave_map[y + 1][x]
        down_left = cave_map[y + 1][x - 1]
        down_right = cave_map[y + 1][x + 1]
        

    cave_map[y][x] = "o"

    source = cave_map[0][source_x]
    part_2_count += 1


print("RESULT 2: ", part_2_count)
