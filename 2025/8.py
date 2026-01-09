import math
from functools import reduce


class Coord:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"Coord({self.x}, {self.y}, {self.z})"

    def distance(self, other: "Coord") -> int:
        """Calculate the distance between this coord and the other coord"""
        return math.sqrt(
            pow((self.x - other.x), 2)
            + pow((self.y - other.y), 2)
            + pow((self.z - other.z), 2)
        )


class Circuit:
    def __init__(self, coord: Coord):
        assert type(coord) == Coord
        self.coords = set([coord])

    def __str__(self):
        return f"Circuit({[str(coord) for coord in self.coords]})"

    def add_coord(self, new_coord: Coord) -> "Circuit":
        """Adds a new coordinate to this circuit and returns new circuit for convenience"""
        self.coords.add(new_coord)
        return self

    def contains(self, target: Coord) -> bool:
        """Is the given coord in this circuits coords?"""
        return target in self.coords

    def get_size(self) -> int:
        """Get the size of this circuit"""
        return len(self.coords)

    def merge_in_circuit(self, other: "Circuit") -> None:
        self.coords = self.coords.union(other.coords)


def find_closest_pair(
    distance_map: dict[Coord, list[float]],
) -> tuple[Coord, int, float]:
    """Finds the closest pair and returns a tuple in the form of (Coord1, index of closest coord in dict[coord1])"""

    coord = None
    overall_min_distance = math.inf
    overall_min_distance_index = None
    for this_coord, distances in distance_map.items():
        if len(distances) == 0:
            continue

        this_distance_index, this_min_distance = min(
            enumerate(distances), key=lambda x: x[1]
        )
        if this_min_distance < overall_min_distance:
            overall_min_distance = this_min_distance
            overall_min_distance_index = this_distance_index
            coord = this_coord

    return (coord, overall_min_distance_index)


def merge_and_grow(
    circuit_to_grow: Circuit,
    other_circuits: list[Circuit],
    circuit_groups: list[Circuit],
) -> None:
    """Merge in any of the given circuits and then add the new junction box"""
    for circuit in other_circuits:
        circuit_to_grow.merge_in_circuit(circuit)
        circuit_groups.remove(circuit)


def solution(coords: list[Coord], number_of_groupings: int = None) -> int:
    # O(1) lookup for coord indices
    coord_to_index = {coord: i for i, coord in enumerate(coords)}
    
    # A mapping of coord_x: list of distances between coord_x and all coords further in the list
    distance_map: dict[Coord, list[float]] = {
        coord: [coord.distance(other) for other in coords[coord_to_index[coord] + 1 :]]
        for coord in coords
    }

    circuit_groups: list[Circuit] = [Circuit(coord) for coord in coords]

    coord1 = None
    coord2 = None

    groupings_left = number_of_groupings

    while groupings_left > 0 if groupings_left is not None else len(circuit_groups) > 1:
        coord1, distance_index = find_closest_pair(distance_map)
        coord2 = coords[
            distance_index
            + coord_to_index[coord1]
            + 1  # Weird index due to cascading len(distances) in distance map
        ]

        circuits_with_coords = [
            group
            for group in circuit_groups
            if group.contains(coord1) or group.contains(coord2)
        ]

        if len(circuits_with_coords) == 0:
            raise AssertionError(
                f"Found coords: {str(coord1)} and {str(coord2)} outside of a circuit!\ncircuit_groups: {[str(circuit) for circuit in circuit_groups]}"
            )

        merge_and_grow(
            circuits_with_coords[0],
            circuits_with_coords[1:],
            circuit_groups,
        )

        distance_map[coord1][distance_index] = math.inf

        if groupings_left is not None:
            groupings_left -= 1

    if number_of_groupings is None:
        return coord1.x * coord2.x

    return reduce(
        lambda acc, circuit: acc * circuit.get_size(),
        sorted(circuit_groups, key=lambda circuit: circuit.get_size(), reverse=True)[
            0:3
        ],
        1,
    )


with open("2025/inputs/8.txt") as inpt:
    lines = inpt.readlines()

    coords = [
        Coord(int(x), int(y), int(z)) for x, y, z in [line.split(",") for line in lines]
    ]

    number_of_groupings = 1000
    print(
        f"Solution for part 1 ({number_of_groupings} groupings): ",
        solution(coords, number_of_groupings),
    )
    print("Solution for part 2: ", solution(coords))
