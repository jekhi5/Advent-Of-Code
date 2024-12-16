#!/usr/bin/env python3
import math, sys, copy

loi = None
with open("input.txt") as file:
    loi = file.readlines()
    

pairs = []

for line in loi:
    first_equal = line.find("=")
    first_comma = line.find(",")

    second_equal = line.find("=", first_comma)

    colon = line.find(":")

    third_equal = line.find("=", colon)
    second_comma = line.find(",", third_equal)
    
    fourth_equal = line.find("=", second_comma)


    sX = int(line[first_equal + 1:first_comma])
    sY = int(line[second_equal + 1:colon])

    bX = int(line[third_equal + 1: second_comma])
    bY = int(line[fourth_equal + 1:])

    pairs.append(( (sX, sY), (bX, bY) ))

def calc_dist(pair):
    left = pair[0]
    right = pair[1]

    return abs(left[0] - right[0]) + abs(left[1] - right[1])

distances = list(map(lambda pair: calc_dist(pair), pairs))



LINE_TO_CHECK = 2000000
MAX_COORD = 4000000

part_2 = True

index_of_overlaps = set()
for i in range(len(pairs)):

    dist = distances[i]
    sensor = pairs[i][0]

    y = sensor[1]
    
    # Checks if this sensors radius overlaps with the line we want to check
    if abs(y - LINE_TO_CHECK) <= dist:
        index_of_overlaps.update(range(sensor[0] - (dist - abs(y - LINE_TO_CHECK)), sensor[0] + (dist - abs(y - LINE_TO_CHECK))))


#distress_coords = (-1, -1)
## Loop through every sensor, find the points that surround that, see if all other sensors overlap with that singular point
#for i in range(len(pairs)):
#
#    dist = distances[i] + 1
#    sensor = pairs[i][0]
#    
#    subset_coords = [x for x in pairs if x[0] is not sensor]
#    subset_distances = [distances[i] for i in range(len(distances)) if pairs[i][0] is not sensor]
#    
#    candidates = []
#    
#    # Store all of the coordinates lying just outside this sensors range
#    for y in range(max(sensor[1] - dist, 0), min(sensor[1] + dist, MAX_COORD)):
#        lower_x = sensor[0] - (dist - abs(sensor[1] - y))
#        upper_x = sensor[0] + (dist - abs(sensor[1] - y))
#
#        lower_coord = (lower_x, y)
#        upper_coord = (upper_x, y)
#
#        candidates.append(lower_coord)
#        candidates.append(upper_coord)
#    ##print("candidates: ", candidates)
#    ##print()
#    
#    # For every OTHER sensor, see if it overlaps with any of the candidates.  If so, remove it from the list of candidates
#    for j in range(len(subset_coords)):
#        sub_dist = subset_distances[j]
#        sub_sensor = subset_coords[j][0]
#        ##print("sub_sensor: ", sub_sensor)
#        ##print("sub_dist: ", sub_dist)
#        bounds = []
#        for y in range(sub_sensor[1] - sub_dist, sub_sensor[1] + sub_dist):
#            # The candidates at the current y value
#            candidates_at_y = list(filter(lambda coord: coord[1] == y, candidates))
#            
#           
#            ##print("candidates_at_y: ", candidates_at_y) 
#            
#
#            # The lower and upper bound of the x coordinate of this sensor at this y value
#            lower_x_bound = sub_sensor[0] - (sub_dist - abs(sub_sensor[1] - y))
#            upper_x_bound = sub_sensor[0] + (sub_dist - abs(sub_sensor[1] - y))
#            bounds.append( [lower_x_bound, upper_x_bound] )
#            # The bad coordinates are any candidates whose y-value is equal to the current y-value, and whose x-value falls within the span of this sensor's view
#            bad_coords = list(filter(lambda coord: coord[0] >= lower_x_bound and coord[0] <= upper_x_bound, candidates_at_y))
#
#            # Now filter out the bad coordinates
#            candidates = list(filter(lambda coord: not coord in bad_coords, candidates))
#            #if y == 11:
#                ##print("y: ", y)
#                ##print("bounds: ", bounds)
#                ##print("updated candidates: ", candidates)
#        if len(candidates) == 1:
#            distress_coords = candidates[0]
#    ##print("----------")

#distress_coords = (-1, -1)
#cur_x = 0
#cur_y = 0
#not_seen = True
#
#starting_coords = set()
#starting_coords.add( (cur_x, cur_y) )
#while not_seen:
#    sensors_seeing_cur = []
#    dists_of_sensor = []
#    for i in range(len(pairs)):
#        sensor = pairs[i][0]
#        dist = distances[i]
#        
#        lower_x_bound = sensor[0] - (dist - abs(sensor[1] - cur_y))
#        upper_x_bound = sensor[0] + (dist - abs(sensor[1] - cur_y))
#
#        if cur_x >= lower_x_bound and cur_x <= upper_x_bound:
#            sensors_seeing_cur.append(sensor)
#            dists_of_sensor.append(dist)
#    
#    if len(sensors_seeing_cur) == 0:
#        distress_coords = (cur_x, cur_y)
#        not_seen = False
#    else:
#        
#        size_before = len(starting_coords)
#        print("LIST OF SEEING SENSORS: ", sensors_seeing_cur)
#        
#        for i in range(len(sensors_seeing_cur)):
#            sensor_seeing_cur = sensors_seeing_cur[i]
#            dist_of_sensor = dists_of_sensor[i]
#
#            print("seeing sensor: ", sensor_seeing_cur)
#            print("dist: ", dist_of_sensor)
#            
#            # We now want to pick new starting coordinates. We want to ensure that these starting 
#            # coordiantes are not ones that we've starting at before, otherwise we will loop infinetely.
#            # We also want to extend the range on the y-axis by one on either side to be sure to include those edges.
#            # The plus 2 on the upper bound is because the upper range is exclusive.
#            for y in range(max(sensor_seeing_cur[1] - (dist_of_sensor + 1), 0), min(sensor_seeing_cur[1] + dist_of_sensor + 2, MAX_COORD)):
#                
#                # This handles the case where we extend beyond the tops and bottoms of the range on the y-axis
#                span = max(dist_of_sensor - abs(sensor_seeing_cur[1] - y), 0)
#                lower_x = sensor_seeing_cur[0] - span
#                upper_x = sensor_seeing_cur[0] + span
#                
#                lower_coord = (lower_x, y)
#                upper_coord = (upper_x, y)
#                print("y: ", y)
#                print("lower_coord: ", lower_coord)
#                print("upper_coord: ", upper_coord)
#
#
#                if lower_coord not in starting_coords and lower_x >= 0 and lower_x <= MAX_COORD:
#                    print("USING LOWER COORD")
#                    cur_x = lower_coord[0]
#                    cur_y = lower_coord[1]
#                    starting_coords.add(lower_coord)
#                    break
#                elif upper_coord not in starting_coords and upper_x >= 0 and upper_x <= MAX_COORD:
#                    print("USING UPPER COORD")
#                    cur_x = upper_coord[0]
#                    cur_y = upper_coord[1]
#                    starting_coords.add(upper_coord)
#                    break
#            
#            if len(starting_coords) != size_before:
#                break
#
#        print("starting_coords: ", starting_coords)        
#        
#        if len(starting_coords) == size_before:
#            raise Exception("Error! No new starting coordiantes were added!")
#
#        print("-----------")
#        print()

distress_coords = (-1, -1)
for y in range(MAX_COORD):
    ranges = []
    for i in range(len(pairs)):
        sensor = pairs[i][0]
        dist = distances[i]
        
        if dist - abs(sensor[1] - y) > 0:
            ranges.append([max(0, sensor[0] - max(dist - abs(sensor[1] - y), 0)), min(MAX_COORD, sensor[0] + max(dist - abs(sensor[1] - y), 0))])
    
    ranges = list(sorted(ranges, key=lambda x: x[0]))
    master_range = ranges[0]
    for i in range(1, len(ranges)):
        new = ranges[i]
        
        # Master range is fully enveloped by the new range
        if new[0] <= master_range[0] and new[1] >= master_range[1]:
            master_range = new

        # The new range starts lower than the master range but the master range ends higher
        elif new[0] <= master_range[0] and (new[1] <= master_range[1] and new[1] >= master_range[0]):
            master_range = (new[0], master_range[1])

        # The new range is fully enveloped by the master range
        elif (new[0] >= master_range[0] and new[0] <= master_range[1]) and new[1] <= master_range[1]:
            pass

        # The master range starts lower than the new range, but the new range ends higher
        elif master_range[0] <= new[0] and master_range[1] >= new[0] and new[1] >= master_range[1]:
            master_range = (master_range[0], new[1])
        else:
            new_x = min(new[1], master_range[1]) + 1
            distress_coords = (new_x, y)
            break

    if distress_coords != (-1, -1):
        break

print(len(index_of_overlaps))
print("Distress Coordinates: ",  distress_coords)
print((distress_coords[0] * 4000000) + distress_coords[1])
