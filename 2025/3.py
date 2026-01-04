def find_max_joltage(line: str, max_digits: int) -> int:
    stack = [line[0]]

    for index, cur_digit_as_string in enumerate(list(line)):
        if index == 0:
            continue

        while (
            len(stack) > 0
            and int(cur_digit_as_string) > int(stack[-1])
            # There are enough digits after this one to make a long enough digit:
            and len(stack) + (len(line) - (index)) > max_digits
        ):
            stack.pop()

        stack.append(cur_digit_as_string)

    return int("".join(stack[0:max_digits]))


def solution(lines: list[str], num_digits: int) -> int:
    total = 0

    for line in lines:
        result = find_max_joltage(line, num_digits)
        total += result

    return total


with open("2025/inputs/3.txt") as inputs:
    lines = inputs.read().splitlines()
    print("Solution for part 1: ", solution(lines, 2))
    print("Solution for part 2: ", solution(lines, 12))
