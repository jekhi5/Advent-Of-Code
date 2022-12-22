#!/usr/bin/env python3
import math, sys, copy
from functools import cmp_to_key

file = open("input.txt")
loi = file.readlines()

def build_list(inpt):
    cur_list = []
    skip_amt = 0
    for i in range(1, len(inpt)):
        if skip_amt > 0:
            skip_amt -= 1
            continue
        elif str.isdigit(inpt[i]):
            next_comma = sys.maxsize if inpt.find(",", i) == -1 else inpt.find(",", i)
            next_closing_brace = inpt.find("]", i)
            next_token = min(next_comma, next_closing_brace)

            full_num = inpt[i:next_token]
            cur_list.append(int(full_num))
            skip_amt = len(full_num) - 1
        elif inpt[i] == "[":
            inner_list = build_list(inpt[i:])
            cur_list.append(inner_list)

            count = 1
            for j in range(i + 1, len(inpt)):
                if inpt[j] == "[":
                    count += 1
                elif inpt[j] == "]":
                    count -= 1

                if count == 0:
                    skip_amt = j - i
                    break

            if count != 0:
                raise Exception(f'Error! Mistep creating list! inner_list: {inner_list}. cur_list: {cur_list}')
            
        elif inpt[i] == "]":
            return [x for x in cur_list]

    raise Exception(f'Error didn\'t reach base case. cur_list: {cur_list}')

result = []
cur_pair = []

for line in loi:
    if line.startswith("["):
        cur_pair.append(build_list(line))
    else:
        result.append((cur_pair[0], cur_pair[1]))
        cur_pair = []

result.append((cur_pair[0], cur_pair[1]))
file.close()


def is_in_order(left, right):
#    print("LEFT: ", left)
#    print("RIGHT: ", right)
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return 1
        if left == right:
            return 0
        if left < right:
            return -1
    elif isinstance(left, int) and isinstance(right, list):
        return is_in_order([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return is_in_order(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            status = is_in_order(left[i], right[i])
                
            if status == 1 or status == -1:
                return status
                
        if len(left) < len(right):
            return -1
        if len(left) == len(right):
            return 0
        if len(left) > len(right):
            return 1
    else:
        raise Exception("BAD TYPE")

total = 0

for i in range(len(result)):
    pair = result[i]

    if is_in_order(pair[0], pair[1]) == -1:
 #       print("IN ORDER: ", i + 1)
        total += i + 1


sorted_packets = [x for t in result for x in t]
sorted_packets.append([[2]])
sorted_packets.append([[6]])
sorted_packets = list(sorted(sorted_packets, key=cmp_to_key(is_in_order)))


print(total)
print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
