from __future__ import annotations
from collections import deque
from dataclasses import dataclass, field
from typing import NamedTuple

TEST_DATA = """.#.
..#
###"""
CHALLENGE_DATA = """....###.
#...####
##.#.###
..#.#...
##.#.#.#
#.######
..#..#.#
######.#"""


class Coord(NamedTuple):
    x: int
    y: int
    z: int

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y, self.z + other.z)


@dataclass
class PowerGrid:
    active_cells: set[Coord] = field(default_factory=set)
    neighbor_references: set[Coord] = field(default_factory=set)

    def __init__(self, grid_map: str):
        self.active_cells = set()
        for y, row in enumerate(grid_map.split()):
            for x, value in enumerate(row):
                new_coord = Coord(x, y, 0)
                if value == "#":
                    self.active_cells.add(new_coord)

        ints = {-1, 0, 1}
        self.neighbor_references = {Coord(x, y, z) for x in ints for y in ints for z in ints
                                    if not (x, y, z) == (0, 0, 0)}

    @property
    def active_count(self):
        return len(self.active_cells)

    def next_state(self):
        check_coords = deque(self.active_cells)
        checked = set()
        new_active = set()
        while check_coords:
            position = check_coords.popleft()
            neighbors = {position + reference for reference in self.neighbor_references}
            active_neighbors = 0
            for neighbor in neighbors:
                if neighbor in self.active_cells:
                    active_neighbors += 1
                if neighbor not in checked and position in self.active_cells:
                    check_coords.append(neighbor)
            if position in self.active_cells and active_neighbors in {2, 3}:
                new_active.add(position)
            elif position not in self.active_cells and active_neighbors == 3:
                new_active.add(position)
            checked.add(position)

        self.active_cells = new_active

    def run_cycles(self, iterations: int):
        for _ in range(iterations):
            self.next_state()
        print(self.active_count)


if __name__ == '__main__':
    # test_grid = PowerGrid(TEST_DATA)
    # test_grid.run_cycles(6)

    true_grid = PowerGrid(CHALLENGE_DATA)
    true_grid.run_cycles(6)
