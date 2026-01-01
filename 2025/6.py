import re
from typing import Callable
from functools import reduce
import numpy as np


class Problem:
    def __init__(self, nums: list[int] = [], op: Callable[[int, int], int] = None):
        self.nums = nums
        self.op = op

    def add_num(self, new_num: int):
        self.nums.append(new_num)

    def set_op(self, op: Callable[[int, int], int]):
        self.op = op

    def solve(self):
        return reduce(self.op, self.nums)

    def __str__(self):
        return f"Problem({self.nums},{self.op})"


def set_string_op(op: str, problem: Problem):
    if op == "+":
        problem.set_op(lambda x, y: x + y)
    elif op == "-":
        problem.set_op(lambda x, y: x - y)
    elif op == "*":
        problem.set_op(lambda x, y: x * y)
    elif op == "/":
        problem.set_op(lambda x, y: x / y)
    else:
        raise ValueError("Unknown type")


def solution(problems: list[Problem]):
    return sum([problem.solve() for problem in problems])


with open("2025/inputs/6.txt") as inpt:
    lines = inpt.readlines()
    problems: list[Problem] = []
    # The list of potential expected ops at the start of a line
    op_pattern = re.compile("\+|/|\*|-")
    for line in lines:
        tokens = [token.strip() for token in line.split(" ") if token.strip() != ""]
        if op_pattern.match(line[0]) != None:
            for op, problem in zip(tokens, problems):
                set_string_op(op, problem)
        else:
            for new_num, i in zip(tokens, range(len(tokens))):
                if i >= len(problems):
                    problems.append(Problem([int(new_num)]))
                else:
                    problems[i].add_num(int(new_num))

    print("Solution for part 1: ", solution(problems))


inpt = np.genfromtxt("2025/inputs/6.txt", dtype="U1", delimiter=1)

problem_numbers = []
cur_problem_numbers = []
for col in range(inpt.shape[1]):
    column = list(inpt[:, col])
    if "".join(column).strip() == "":
        problem_numbers.append(cur_problem_numbers)
        cur_problem_numbers = []

    new_num = "".join([digit for digit in column if digit in "1234567890"])
    if new_num != "":
        cur_problem_numbers.append(int(new_num))

problem_numbers.append(cur_problem_numbers)

problems = []
for problem_numbers in problem_numbers:
    problems.append(Problem(problem_numbers))

ops = [op_string.strip() for op_string in inpt[-1, :] if op_string.strip() != ""]
for op, problem in zip(ops, problems):
    set_string_op(op, problem)

print("Solution for part 2: ", solution(problems))
