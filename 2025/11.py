from __future__ import annotations


def find_total_paths(
    node_connections: list[int],
    node_index: int,
    memo_table: dict[tuple[int, frozenset[int]], tuple[int, int]],
    nodes: list[list[int]],
    found_targets: frozenset[int],
    target_indices: frozenset[int],
) -> tuple[int, int]:
    out = len(nodes)

    if node_index in target_indices:
        found_targets = found_targets.union({node_index})

    # Check memo with state
    memo_key = (node_index, found_targets)
    if memo_key in memo_table:
        return memo_table[memo_key]

    this_node_total_paths = 0
    this_node_total_paths_with_problem_nodes = 0
    for connection in node_connections:
        if connection == out:
            this_node_total_paths += 1
            if found_targets == target_indices:
                this_node_total_paths_with_problem_nodes += 1
        else:
            total_paths_from_here, total_problem_paths_from_here = find_total_paths(
                nodes[connection],
                connection,
                memo_table,
                nodes,
                found_targets,
                target_indices,
            )
            this_node_total_paths += total_paths_from_here
            this_node_total_paths_with_problem_nodes += total_problem_paths_from_here

    result = (this_node_total_paths, this_node_total_paths_with_problem_nodes)
    memo_table[memo_key] = result
    return result


def solution(
    lines: list[str], starting_node: str, target_nodes: list[str] | None = None
) -> int:
    if target_nodes is None:
        target_nodes = []
    # string_nodes is a straight dictionary representation of the input, sorted alphabetically
    string_nodes = {
        node.split(":")[0]: [
            conn.strip() for conn in node.split(":")[1].split(" ") if conn != ""
        ]
        for node in sorted(
            lines,
            key=lambda line: (
                "" if line.split(":")[0] == starting_node else line.split(":")[0]
            ),
        )
    }

    # This will allow us to use indices rather than the string names, with "you" at
    # index 0 and "out" at index len(nodes)
    name_mapping = {name: index for index, name in enumerate(string_nodes.keys())}
    out_index = len(name_mapping)
    node_names = list(string_nodes.keys())
    target_indices = frozenset(
        node_names.index(target_node) for target_node in target_nodes
    )
    name_mapping["out"] = out_index

    # The index in the nodes array is the node referenced in the connections
    nodes = [
        [name_mapping[connection] for connection in connections]
        for connections in string_nodes.values()
    ]

    # The memo table contains information about how many paths each node (represented by the index)
    # has to the "out" node as follows: (path_distance_total, path_distance_with_all_target_nodes)
    memo_table = {}

    result = find_total_paths(
        nodes[0],
        0,
        memo_table,
        nodes,
        frozenset(),
        target_indices,
    )

    return result[0 if target_indices is None else 1]


with open("2025/inputs/11.txt") as inpt:
    lines = inpt.readlines()

    print("Solution for part 1: ", solution(lines, "you"))
    print("Solution for part 2: ", solution(lines, "svr", ["dac", "fft"]))
