#!/usr/bin/env python3
import math, sys, copy

loi = None
with open("input.txt") as file:
    loi = file.readlines()

# Graph syntax:

# {"String node name" : {"total_pressure_release": [list of n pressures where each index, i, stores (weight * (n - i)) indicating the total pressure released if the valvue was released at minute i],
#                        "edges": [List of edge names],
#                        "valve_open": True/False
#                        "max_value": The most pressure that can be released upon reaching this node. Will be updated as the algorithm processes}
#  ....}

graph = {}

MINUTES = 30

for line in loi:
    name = line[6:8]

    init_rate = int(line[line.find("=") + 1:line.find(";")])
    
    # Fill the rates array by decreasing the amount of total pressure that would be released based on what minute it was released at
    rates = [init_rate * (MINUTES - x) for x in range(MINUTES)]

    neighbors = line.split(",")
    neighbors[0] = neighbors[0][len(neighbors[0]) - 2:]

    neighbors = list(map(lambda x: x.strip(), neighbors))

    graph[name] = {"total_pressure_release": rates,
                   "edges": neighbors,
                   "valve_open": False
                   "max_value": -1}


for key, val in graph.items():
    print(key, " : ", val)



