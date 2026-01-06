manifold = []
memoized_manifold = []


def find_ceiling_splitter(row: int, col: int) -> int:
    for cur_row in range(row - 1, 0, -1):
        if manifold[cur_row][col] != ".":
            return cur_row

    return 0


def sum_above_timelines(row: int, col: int) -> int:
    ceiling_splitter_row = find_ceiling_splitter(row, col)

    # This is the first splitter and there is only one particle that can pass through it
    if ceiling_splitter_row == 0 and manifold[0][col] == "S":
        return 1

    total = 0
    for cur_row in range(row - 1, ceiling_splitter_row, -1):
        left = memoized_manifold[cur_row][col - 1] if col > 0 else None
        right = (
            memoized_manifold[cur_row][col + 1]
            if col < len(memoized_manifold[cur_row]) - 1
            else None
        )
        total += left if left != None else 0
        total += right if right != None else 0

    return total


def find_total_timelines() -> int:
    for i, row in enumerate(manifold):
        for j, spot in enumerate(row):
            if spot == "^":
                memoized_manifold[i][j] = sum_above_timelines(i, j)

    return sum(
        [
            sum_above_timelines(len(manifold) - 1, col)
            for col in range(len(manifold[-1]))
        ]
    )


def find_total_splits(cur_row, beam_col):
    if cur_row == len(manifold) - 1 or manifold[cur_row + 1][beam_col] == "|":
        # End of manifold or overlapping beam
        return 0
    if manifold[cur_row + 1][beam_col] == ".":
        # No splitter, move straight down
        manifold[cur_row + 1][beam_col] = "|"
        return find_total_splits(cur_row + 1, beam_col)
    if manifold[cur_row + 1][beam_col] == "^":
        # Split
        if beam_col == 0:
            # On left edge
            # Don't overlap with existing beams to the RIGHT
            if manifold[cur_row + 1][beam_col + 1] == "|":
                return 1

            manifold[cur_row + 1][beam_col + 1] = "|"
            return find_total_splits(cur_row + 1, beam_col + 1) + 1
        elif beam_col == len(manifold[cur_row]) - 1:
            # On right edge
            # Don't overlap with existing beams to the LEFT
            if manifold[cur_row + 1][beam_col - 1] == "|":
                return 1

            manifold[cur_row + 1][beam_col - 1] = "|"
            return find_total_splits(cur_row + 1, beam_col - 1) + 1
        else:
            # Somewhere in the middle of the manifold
            if (
                manifold[cur_row + 1][beam_col - 1] == "|"
                and manifold[cur_row + 1][beam_col + 1] == "|"
            ):
                # Both sides of splitter already have a beam
                return 1
            elif manifold[cur_row + 1][beam_col - 1] == "|":
                # Left side of splitter already had a beam, just set right
                manifold[cur_row + 1][beam_col + 1] = "|"
                return find_total_splits(cur_row + 1, beam_col + 1) + 1
            elif manifold[cur_row + 1][beam_col + 1] == "|":
                # Right side of splitter already had a beam, just set left
                manifold[cur_row + 1][beam_col - 1] = "|"
                return find_total_splits(cur_row + 1, beam_col - 1) + 1
            else:
                # Both sides need a splitter
                manifold[cur_row + 1][beam_col - 1] = "|"
                manifold[cur_row + 1][beam_col + 1] = "|"
                return (
                    find_total_splits(cur_row + 1, beam_col - 1)
                    + find_total_splits(cur_row + 1, beam_col + 1)
                    + 1
                )
    raise ValueError(f"Illegal manifold state: {manifold}")


with open("2025/inputs/7.txt") as inpt:
    lines = inpt.read().splitlines()

    manifold = [list(line) for line in lines]
    starting_beam_col = "".join(manifold[0]).find("S")
    print("Solution for part 1: ", find_total_splits(0, starting_beam_col))
    manifold = [list(line) for line in lines]
    memoized_manifold = [
        [0 if char == "^" else None for char in row] for row in manifold
    ]

    print("Solution for part 2: ", find_total_timelines())
