def fill_lps_memo_table(string, string_length, memo_table):
    prev_length = 0
    i = 1
    memo_table[0] = 0

    while i < string_length:
        if string[i] == string[prev_length]:
            prev_length += 1
            memo_table[i] = prev_length
            i += 1
        else:
            if prev_length != 0:
                prev_length = memo_table[prev_length - 1]
            else:
                memo_table[i] = 0
                i += 1


def is_invalid(id, part=1):
    id = str(id)

    if part == 1:
        if len(id) % 2 == 1:
            return False

        for i in range(1, (int(len(id) / 2)) + 1):
            if id[:i] == id[i:]:
                return True
        return False
    else:
        length = len(id)
        longest_prefix_suffix_memo = [0 for _ in range(length)]

        fill_lps_memo_table(id, length, longest_prefix_suffix_memo)

        # has to be at least two repeats
        return (
            longest_prefix_suffix_memo[-1] > 0
            and length % (length - longest_prefix_suffix_memo[-1]) == 0
        )


def count_invalid_in_range(start, end, part=1):
    count = 0
    for id in range(start, end + 1):
        count += id if is_invalid(id, part) else 0

    return count


def solution(ranges, part=1):
    count = 0
    for range in ranges:
        start, end = range.split("-")
        count += count_invalid_in_range(int(start), int(end), part)

    return count


file = open("2025/inputs/2.txt")
lines = file.read().split(",")
file.close()

print("Solution for part 1: ", solution(lines, 1))
print("Solution for part 2: ", solution(lines, 2))
