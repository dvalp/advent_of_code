from itertools import zip_longest
from typing import Iterable, Set, Tuple


def calculate_wires() -> int:
    with open("input_day03", "r") as f:
        wires = [tuple(line.strip().split(",")) for line in f]

    start_pos = (0, 0)
    current_pos = start_pos
    coords_a = [start_pos]
    for segment in wires[0]:
        new_positions, current_pos = add_coords(segment, current_pos)
        coords_a.extend(new_positions)

    current_pos = start_pos
    coords_b = [start_pos]
    for segment in wires[1]:
        new_positions, current_pos = add_coords(segment, current_pos)
        coords_b.extend(new_positions)

    intersections = (set(coords_a) & set(coords_b))
    intersections.discard((0, 0))

    # return the Manhattan distance of the closest non-zero intersection
    return min((coords_a.index(intersection) + coords_b.index(intersection)) for intersection in intersections)


def add_coords(entry: str, current_pos: Tuple[int, int]) -> Tuple[Iterable[Tuple[int, int]], Tuple[int, int]]:
    """
    Expects new entry of form like "R75" where:
        First position is a char of R, L, D, U
        Remaining is an integer for the number of steps to add
    R: Add position 0
    L: Subtract position 0
    U: Add position 1
    D: Subtract position 1
    """
    operation = entry[0]
    n = int(entry[1:])
    if entry[0] in ['D', 'L']:
        num_steps = (n + 1) * (-1)
        increment = -1
    else:
        num_steps = (n + 1)
        increment = 1

    if operation in ["R", "L"]:
        coord_var = current_pos[0]
        coord_static = current_pos[1]
        upper_limit = coord_var + num_steps
        coords = zip_longest(range(coord_var + increment, upper_limit, increment), [], fillvalue=coord_static)
        new_pos = (coord_var + (n * increment), coord_static)
    else:
        coord_var = current_pos[1]
        coord_static = current_pos[0]
        upper_limit = coord_var + num_steps
        coords = zip_longest([], range(coord_var + increment, upper_limit, increment), fillvalue=coord_static)
        new_pos = (coord_static, coord_var + (n * increment))

    return coords, new_pos


def calculate_wires_first_star() -> int:
    with open("input_day03", "r") as f:
        wires = [tuple(line.strip().split(",")) for line in f]

    start_pos = (0, 0)
    current_pos = start_pos
    coords_a = {start_pos}
    for segment in wires[0]:
        new_positions, current_pos = add_coords(segment, current_pos)
        coords_a.update(new_positions)

    current_pos = start_pos
    coords_b = {start_pos}
    for segment in wires[1]:
        new_positions, current_pos = add_coords(segment, current_pos)
        coords_b.update(new_positions)

    intersections = (coords_a & coords_b)
    totals = [sum((abs(coord[0]), abs(coord[1]))) for coord in intersections]

    # return the Manhattan distance of the closest non-zero intersection
    return sorted(zip(totals, intersections))[1][0]


def add_coords_first_star(entry: str, current_pos: Tuple[int, int]) -> Tuple[Set[Tuple[int, int]], Tuple[int, int]]:
    """
    Expects new entry of form like "R75" where:
        First position is a char of R, L, D, U
        Remaining is an integer for the number of steps to add
    R: Add position 0
    L: Subtract position 0
    U: Add position 1
    D: Subtract position 1
    """
    operation = entry[0]
    n = int(entry[1:])
    if entry[0] in ['D', 'L']:
        num_steps = (n + 1) * (-1)
        increment = -1
    else:
        num_steps = (n + 1)
        increment = 1

    if operation in ["R", "L"]:
        coord_var = current_pos[0]
        coord_static = current_pos[1]
        upper_limit = coord_var + num_steps
        coords = set(zip_longest(range(coord_var, upper_limit, increment), [], fillvalue=coord_static))
        new_pos = (coord_var + (n * increment), coord_static)
    else:
        coord_var = current_pos[1]
        coord_static = current_pos[0]
        upper_limit = coord_var + num_steps
        coords = set(zip_longest([], range(coord_var, upper_limit, increment), fillvalue=coord_static))
        new_pos = (coord_static, coord_var + (n * increment))

    return coords, new_pos
