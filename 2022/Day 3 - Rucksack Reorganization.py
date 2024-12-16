#!/usr/bin/env python3
file = open("input.txt")
loi = file.readlines()
file.close()

def Solution(list_of_sacks):
    total = 0
    for sack in list_of_sacks:
        half = int(len(sack) / 2) if len(sack) % 2 == 0 else int((len(sack) + 1) / 2)
        first_half = sack[:half - 1]
        second_half = sack[half - 1:]
        
        common = None
        for letter in first_half:
            if letter in second_half:
                common = letter
                num = ord(common)
                if num > 96 and num < 123:
                    num = num - 96
                else:
                    num = num - 38

                total += num
                break


    return total


print(Solution(loi))


# PART 2


def Solution2(list_of_sacks):
    total = 0
    for i in range(0, len(list_of_sacks), 3):
        
        sack1 = list_of_sacks[i]
        sack2 = list_of_sacks[i + 1]
        sack3 = list_of_sacks[i + 2]
        
        common = None
        for letter in sack1:
            if letter in sack2 and letter in sack3:
                common = letter
                num = ord(common)
                if num > 96 and num < 123:
                    num = num - 96
                else:
                    num = num - 38

                total += num
                break


    return total

print(Solution2(loi))
