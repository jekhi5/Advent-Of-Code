#!/usr/bin/env python3

file = open("input.txt")
loi = file.read()

loi = loi.split("Monkey ")
del loi[0]
file.close()

class Monkey:
    def __init__(self, items, op, test_num, true_monkey, false_monkey, items_handled):
        self.items = items
        self.op = op
        self.test_num = test_num
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.items_handled = items_handled

def make_fund(str_inpt):

    split = str_inpt.split(" ")
    if split[0] == "*" and split[1] == "old":
        return lambda x: x * x
    if split[0] == "+":
        return lambda x: x + int(split[1])
    if split[0] == "*":
        return lambda x: x * int(split[1])
    if split[0] == "-":
        return lambda x: x - int(split[1]) 
    if split[0] == "/":
        return lambda x: x / int(split[1])


def Solution(inpt, rounds, able_to_relax):

    situation = {}
    total_test_num = 1
    for monkey in inpt:
        lines = monkey.split("\n")

        name = lines[0][:-1]
        items = lines[1].split(",")
        items[0] = items[0][items[0].find(":") + 2:]
        items = list(map(int, items))

        operation = make_fund(lines[2][lines[2].find("=") + 6:])

        test_num = int(lines[3].split(" ")[-1])
        total_test_num *= test_num
        true_monkey = lines[4].split(" ")[-1]
        false_monkey = lines[5].split(" ")[-1]

        situation[name] = Monkey(items, operation, test_num, true_monkey, false_monkey, 0)


    for i in range(rounds):
        for monkey in situation.values():
            for item in monkey.items:
                post_inspection = monkey.op(item)

                if able_to_relax:
                    post_relax = post_inspection // 3
                    if post_relax % monkey.test_num == 0:
                        situation[monkey.true_monkey].items.append(post_relax)
                    else:
                        situation[monkey.false_monkey].items.append(post_relax)
                else:
                    if post_inspection % monkey.test_num == 0:
                        situation[monkey.true_monkey].items.append(post_inspection % total_test_num)
                    else:
                        situation[monkey.false_monkey].items.append(post_inspection % total_test_num)

            monkey.items_handled += len(monkey.items)
            monkey.items = []


    sorted_situation = sorted(situation, key=lambda x: situation[x].items_handled, reverse=True)
    return situation[sorted_situation[0]].items_handled * situation[sorted_situation[1]].items_handled

print(Solution(loi, 20, True))
print(Solution(loi, 10000, False))
