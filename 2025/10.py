import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def clicks_for_joltage_config(
    target_joltage: list[int],
    buttons: list[list[int]],
) -> int:
    """
    This was all so new to me, but it's a linear programming
    solution. I originally tried to solve this in a DP way
    with symbol-based solving of a system of equations, but
    it took way too long no matter how I implemented it
    """
    num_counters = len(target_joltage)
    num_buttons = len(buttons)

    # Build constraint matrix where constraint_matrix[j][i] = 1 if button i affects counter j
    constraint_matrix = np.zeros((num_counters, num_buttons), dtype=float)
    for button_idx, button in enumerate(buttons):
        for counter_idx in button:
            constraint_matrix[counter_idx][button_idx] = 1

    target_joltage_np = np.array(target_joltage, dtype=float)

    # Goal: minimize sum of all button presses
    button_len_ones = np.ones(num_buttons)

    # Set the constraints to be exactly equal to the target joltage (upper and lower bounds are the same)
    constraints = LinearConstraint(
        constraint_matrix, target_joltage_np, target_joltage_np
    )

    # All variables are integer, x >= 0
    integrality = np.ones(num_buttons)
    bounds = Bounds(0, np.inf)

    result = milp(
        c=button_len_ones,
        constraints=constraints,
        integrality=integrality,
        bounds=bounds,
    )

    if result.success:
        x_int = np.round(result.x).astype(int)
        return int(np.sum(x_int))

    raise ValueError(f"Could not find integer solution for target {target_joltage}")


def clicks_for_light_config(
    target_light_config: list[bool],
    buttons: list[list[int]],
) -> int:
    memo_table = [{}] * len(buttons)
    first_group = {}
    for button in buttons:
        starting_config = [False] * len(target_light_config)
        for index in button:
            starting_config[index] = not starting_config[index]
        first_group[frozenset([button])] = starting_config

    memo_table[0] = first_group

    if target_light_config in memo_table[0].values():
        return 1

    # We start the enumeration at 1 because it represents the group size for each button-press group
    for i, groups_of_same_size in enumerate(memo_table, 1):
        new_groups = {}
        for button in buttons:
            for group in groups_of_same_size:
                if (button in group) or (group.union([button]) in new_groups):
                    continue
                past_result = groups_of_same_size[group]
                new_result = [light_status for light_status in past_result]
                for index in button:
                    new_result[index] = not new_result[index]
                assert len(new_result) == len(target_light_config)
                if new_result == target_light_config:

                    return i + 1

                new_key = group.union([button])
                new_groups[new_key] = new_result

        memo_table[i] = new_groups

    raise RuntimeError("Did not find valid button combination")


def solution(lines: str) -> tuple[int, int]:
    total_for_lights = 0
    total_for_joltage = []
    for line in lines:
        light_goal, buttons_and_joltage = line.split(" ", 1)
        light_goal_bool = [char == "#" for char in light_goal.strip("[]")]
        buttons = [
            tuple(int(n) for n in button_groups.strip("()").split(","))
            for button_groups in buttons_and_joltage.split(" ")[:-1]
        ]
        joltage = [
            int(joltage)
            for joltage in buttons_and_joltage.split(" ")[-1].strip("{}\n").split(",")
        ]

        # The example notes pressing a button twice, however for part 1 this should never be
        # required as that would just undo an action, thus wasting a button press
        total_for_lights += clicks_for_light_config(light_goal_bool, buttons)
        total_for_joltage.append(clicks_for_joltage_config(joltage, buttons))
    return total_for_lights, sum(total_for_joltage)


with open("2025/inputs/10.txt") as inpt:
    lines = inpt
    total_for_lights, total_for_joltage = solution(lines)

    print("Solution for part 1: ", total_for_lights)
    print("Solution for part 2: ", total_for_joltage)
