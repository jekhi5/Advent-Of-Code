from enum import Enum


class Axis(Enum):
    X = 1
    Y = 2


class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: "Coord") -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Coord({self.x}, {self.y})"

    # TODO: This likely isn't sufficient to find what's "inside" the grid
    # TODO: I think I need to find the left, right, top, and bottom "walls" to be able to determine what's available, likely too expensive, tho
    # def find_axis_pair(self, coords: list["Coord"], axis: Axis) -> int:
    #     # print(f"this: {str(self)}")
    #     # print(f"axis: {axis}")
    #     axis_limit = None
    #     if axis == Axis.X:
    #         # will be a list of length 1 containing limit
    #         # Check opposite coord because we want to find the coord that lies on the
    #         # same line as this one
    #         axis_limit = [
    #             coord for coord in coords if (coord != self and coord.y == self.y)
    #         ]
    #         # print(f"x-axis limit coord: {str(axis_limit[0])}")
    #         assert (
    #             len(axis_limit) == 1
    #         ), f"axis_limit: {[str(coord) for coord in axis_limit]}"
    #         return axis_limit[0].x
    #     else:
    #         # will be a list of length 1 containing limit
    #         # Check opposite coord because we want to find the coord that lies on the
    #         # same line as this one
    #         axis_limit = [
    #             coord for coord in coords if (coord != self and coord.x == self.x)
    #         ]
    #         # print(f"x-axis limit coord: {str(axis_limit[0])}")
    #         assert len(axis_limit) == 1, f"{[str(coord) for coord in axis_limit]}"
    #         return axis_limit[0].y
    #     print(f"matching coords: {[str(coord) for coord in axis_limit]}")

    def calculate_valid_area(
        self, other: "Coord", only_red_green: bool, coords: list["Coord"] = None
    ) -> int:

        is_valid = False
        if only_red_green and coords != None:
            # this_x_axis_lim = self.find_axis_pair(coords, Axis.X)
            # this_y_axis_lim = self.find_axis_pair(coords, Axis.Y)
            # other_x_axis_lim = other.find_axis_pair(coords, Axis.X)
            # other_y_axis_lim = other.find_axis_pair(coords, Axis.Y)
            # print("-------")
            # print(f"this coord: {str(self)}")
            # print(f"other coord: {str(other)}")
            # print(f"this_x_axis_lim: {str(this_x_axis_lim)}")
            # print(f"this_y_axis_lim: {str(this_y_axis_lim)}")
            # print(f"other_x_axis_lim: {str(other_x_axis_lim)}")
            # print(f"other_y_axis_lim: {str(other_y_axis_lim)}")
            # print(f"coords: {[str(coord) for coord in coords]}")

            # if (
            #     (self.x <= other.x and other.x <= this_x_axis_lim)
            #     or (this_x_axis_lim <= other.x and other.x <= self.x)
            # ) and (
            #     (self.y <= other.y and other.y <= this_y_axis_lim)
            #     or (this_y_axis_lim <= other.y and other.y <= self.y)
            # ):
            #     is_valid = True

            # if y_axis_lim > self.y:
            #     # Rectangle must be above current spot
            #     if other.y >= self.y and x_axis_lim > self.x:
            #         # Rectangle must be to the right of current spot
            #         if other.x >= self.x:
            #             is_valid = True
            #     else:
            #         # Rectangle must be to the left of current spot
            #         if other.x <= self.x:
            #             is_valid = True
            # else:
            #     # Rectangle must be below current spot
            #     if other.y <= self.y and x_axis_lim > self.x:
            #         # Rectangle must be to the right of current spot
            #         if other.x >= self.x:
            #             is_valid = True
            #     else:
            #         # Rectangle must be to the left of current spot
            #         if other.x <= self.x:
            #             is_valid = True

            # if is_valid:
            #     area = self.calculate_valid_area(other, False)
            #     # print(f"VALID! Area: {area}")
            #     # print("-------")
            #     return area
            # # print("-------")
            # return 0  # Rectangle requires non-red/green tiles
            pass
        elif not only_red_green:
            return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)
        else:
            raise ValueError(
                "Cannot find only-red-green area without valid coords list."
            )


def solution(coords: list[Coord], is_part_2: bool) -> int:
    largest_area = 0
    largest_coords = None
    for this_coord in coords:
        for other in coords:
            if this_coord == other:
                continue
            new_area = max(
                largest_area, this_coord.calculate_valid_area(other, is_part_2, coords)
            )
            if new_area > largest_area:
                largest_area = new_area
                largest_coords = [this_coord, other]

    return [largest_area, [str(coord) for coord in largest_coords]]


with open("2025/inputs/9.txt") as inpt:
    lines = inpt.readlines()

    coords = [Coord(int(x), int(y)) for x, y in [line.split(",") for line in lines]]

    print("Solution for part 1: ", solution(coords, False))
    # print("Solution for part 2: ", solution(coords, True))
