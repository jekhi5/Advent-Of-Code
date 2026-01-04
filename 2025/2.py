def fill_lps_memo_table(string: str, string_length: int, memo_table: list[int]) -> None:
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


def is_invalid(id: str, part=1) -> bool:
    if part == 1:
        return len(id) != 1 and id[: int(len(id) / 2)] == id[int(len(id) / 2) :]
    else:
        length = len(id)
        longest_prefix_suffix_memo = [0 for _ in range(length)]

        fill_lps_memo_table(id, length, longest_prefix_suffix_memo)

        # has to be at least two repeats
        return (
            longest_prefix_suffix_memo[-1] > 0
            and length % (length - longest_prefix_suffix_memo[-1]) == 0
        )


def count_invalid_in_range(start: int, end: int, part=1) -> int:
    count = 0
    for id in range(start, end + 1):
        count += id if is_invalid(str(id), part) else 0

    return count


def solution(ranges: list[str], part=1) -> int:
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
