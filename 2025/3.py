def find_max_joltage(line, max_digits):
    stack = [line[0]]
    drops_remaining = len(line) - max_digits

    index = 0

    for cur_digit_as_string in list(line)[1:]:
        dropped = False
        while (
            drops_remaining > 0
            and len(stack) > 0
            and int(cur_digit_as_string) > int(stack[-1])
            # There are enough digits after this one to make a long enough digit:
            and len(stack) + (len(line) - (index + 1)) > max_digits
        ):
            stack.pop()
            dropped = True

        if dropped:
            drops_remaining - 1

        stack.append(cur_digit_as_string)
        index += 1

    return int("".join(stack[0:max_digits]))


def solution(lines, num_digits):
    total = 0

    for line in lines:
        result = find_max_joltage(line, num_digits)
        total += result

    return total


with open("2025/inputs/3.txt") as inputs:
    lines = inputs.read().splitlines()
    print("Solution for part 1: ", solution(lines, 2))
    print("Solution for part 2: ", solution(lines, 12))
