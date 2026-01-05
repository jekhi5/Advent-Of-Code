import operator
from functools import reduce
from typing import Callable

import numpy as np


class Problem:
    def __init__(self, nums: list[int] = [], op: Callable[[int, int], int] = None):
        self.nums = nums
        self.op = op

    def add_num(self, new_num: int) -> None:
        self.nums.append(new_num)

    def set_op(self, op: Callable[[int, int], int]) -> None:
        self.op = op

    def solve(self) -> int:
        return reduce(self.op, self.nums)

    def __str__(self):
        return f"Problem({self.nums},{self.op})"


OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def solution(problems: list[Problem]):
    return sum([problem.solve() for problem in problems])


with open("2025/inputs/6.txt") as inpt:
    lines = inpt.readlines()
    problems: list[Problem] = []
    for line in lines:
        tokens = [token.strip() for token in line.split(" ") if token.strip() != ""]
        if tokens[0] in OPS:
            for op, problem in zip(tokens, problems):
                problem.set_op(OPS[op])
        else:
            for i, new_num in enumerate(tokens):
                if i >= len(problems):
                    problems.append(Problem([int(new_num)]))
                else:
                    problems[i].add_num(int(new_num))

    print("Solution for part 1: ", solution(problems))


inpt = np.genfromtxt("2025/inputs/6.txt", dtype="U1", delimiter=1)

problems = []
cur_problem_numbers = []
for column in inpt.T:
    column = list(column)
    if "".join(column).strip() == "":
        problems.append(Problem(cur_problem_numbers))
        cur_problem_numbers = []

    new_num = "".join([digit for digit in column if digit in "1234567890"])
    if new_num != "":
        cur_problem_numbers.append(int(new_num))

problems.append(Problem(cur_problem_numbers))

ops = [op_string.strip() for op_string in inpt[-1, :] if op_string.strip() != ""]
for op, problem in zip(ops, problems):
    problem.set_op(OPS[op])

print("Solution for part 2: ", solution(problems))
