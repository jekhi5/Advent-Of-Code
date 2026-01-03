def solution(lines, part=1):
    cur_num = 50
    count = 0
    for entry in lines:
        change = -int(entry[1:]) if entry[0] == "L" else int(entry[1:])
        new_num_unbounded = cur_num + change
        next_num = (
            new_num_unbounded
            if 0 <= new_num_unbounded and new_num_unbounded < 100
            else new_num_unbounded % 100
        )
        if part == 1:
            count += 1 if next_num == 0 else 0
        if part == 2:
            if new_num_unbounded <= 0 or new_num_unbounded >= 100:
                passed_zero = int(abs(new_num_unbounded / 100)) + 1
                count += passed_zero if change < 0 and cur_num != 0 else passed_zero - 1

        cur_num = next_num

    return count


file = open("2025/inputs/1.txt")
lines = file.readlines()
file.close()

print("Solution for part 1: ", solution(lines, 1))
print("Solution for part 2: ", solution(lines, 2))
