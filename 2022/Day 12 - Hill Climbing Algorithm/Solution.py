#!/usr/bin/env python3
import math, sys, copy


file = open("input.txt")
string = file.read()
rows = string.split("\n")
del rows[-1]
grid = []

for i in range(len(rows)):
    line = rows[i]
    cur_row = []
    for j in range(len(rows[i])):
        split = [ord(rows[i][j])]
        split = list(map(lambda x: {"val": x, 
                                    "path-length": sys.maxsize, 
                                    "has-visited": False, 
                                    "row": i, 
                                    "col": j, 
                                    "path": []}, split))[0]
        cur_row.append(split)
    
    grid.append(cur_row)

file.close()

start_location = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if chr(grid[i][j]["val"]) == "a" or chr(grid[i][j]["val"]) == "S":
            start_location.append((i, j))

end_row = string.find("E") // len(rows[0])
end_col = (string.find("E") - (string.find("E") // len(rows[0]))) % len(rows[0])
# Vertex vals: Value, path length, was_visited, row, col, path

def BFS(grid, start_array, end_row, end_col):
    shortest_path = sys.maxsize

    for coords in start_array:
        grid1 = copy.deepcopy(grid)
        start_row = coords[0]
        start_col = coords[1]
        queue = []

        grid1[start_row][start_col]["val"] = ord("a")
        grid1[start_row][start_col]["path-length"] = 0
        grid1[start_row][start_col]["has-visited"] = True

        grid1[end_row][end_col]["val"] = ord("z")

        queue.append(grid1[start_row][start_col])
    
        found = False
        while len(queue) > 0 and not found:
            cur = queue.pop(0)
            cur_row = cur["row"]
            cur_col = cur["col"]
            for i in range(4):
                neighbor = None 
                try:
                    if i == 0:
                        if cur_row - 1 > -1:
                            neighbor = grid1[cur_row - 1][cur_col]
                        else:
                            continue
                    if i == 1:
                        if cur_col - 1 > -1:
                            neighbor = grid1[cur_row][cur_col - 1]
                        else:
                            continue
                    if i == 2:
                        neighbor = grid1[cur_row + 1][cur_col]
                    if i == 3:
                        neighbor = grid1[cur_row][cur_col + 1]

                except IndexError: continue
                
                # If the neighbor has been visited, stepping to the neighbor is at most an increase of 1, 
                # and entering this node would be shorter than the current path
                if not neighbor["has-visited"] and (neighbor["val"] - cur["val"] < 2):
                    if neighbor["row"] == end_row and neighbor["col"] == end_col:
                        shortest_path = min(shortest_path, cur["path-length"] + 1)
                        found = True
                        break
                    neighbor["has-visited"] = True
                    neighbor["path-length"] = cur["path-length"] + 1
                    neighbor["path"] = [x for x in cur["path"]]
                    neighbor["path"].append((cur["row"], cur["col"]))
                    queue.append(neighbor)
    return shortest_path

just_S = list(filter(lambda x: chr(grid[x[0]][x[1]]["val"]) == "S", start_location))
print(BFS(grid, just_S, end_row, end_col))
print(BFS(grid, start_location, end_row, end_col))
