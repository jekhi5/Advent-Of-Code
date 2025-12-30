def num_rolls_surrounding(grid, row, col):
    lower_row_bound = max(0, row - 1)
    upper_row_bound = min(len(grid) - 1, row + 1)
    lower_col_bound = max(0, col - 1)
    upper_col_bound = min(len(grid[0]) - 1, col + 1)

    total = 0
    for r in range(lower_row_bound, upper_row_bound + 1):
        for c in range(lower_col_bound, upper_col_bound + 1):
            if r != row or c != col:  # Exclude center cell
                total += grid[r][c]

    return total


def solution(grid, part):
    total_movable_rolls = 0
    removed_roll = True
    while removed_roll == True:
        removed_roll = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and num_rolls_surrounding(grid, i, j) < 4:
                    total_movable_rolls += 1
                    if part == 2:
                        grid[i][j] = 0
                        removed_roll = True

    return total_movable_rolls


with open("2025/inputs/4.txt") as inpt:
    lines = inpt.read().splitlines()
    grid = [list(line) for line in lines]
    num_grid = [[0 if char == "." else 1 for char in line] for line in grid]
    print("Solution for part 1: ", solution(num_grid, 1))
    print("Solution for part 2: ", solution(num_grid, 2))
