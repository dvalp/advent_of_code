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


class Coord4D(NamedTuple):
    x: int
    y: int
    z: int
    w: int

    def __add__(self, other):
        return Coord4D(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)


@dataclass
class PowerGrid:
    active_cells: set[Coord] = field(default_factory=set)
    neighbor_references: set[Coord] = field(default_factory=set)

    @staticmethod
    def parse_data(grid_map: str):
        active_cells = set()
        for y, row in enumerate(grid_map.split()):
            for x, value in enumerate(row):
                new_coord = Coord(x, y, 0)
                if value == "#":
                    active_cells.add(new_coord)

        ints = {-1, 0, 1}
        neighbor_references = {Coord(x, y, z) for x in ints for y in ints for z in ints
                               if not (x, y, z) == (0, 0, 0)}
        return PowerGrid(active_cells=active_cells, neighbor_references=neighbor_references)

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


@dataclass
class PowerGrid4D(PowerGrid):
    active_cells: set[Coord4D] = field(default_factory=set)
    neighbor_references: set[Coord4D] = field(default_factory=set)

    @staticmethod
    def parse_data(grid_map: str):
        active_cells = set()
        for y, row in enumerate(grid_map.split()):
            for x, value in enumerate(row):
                new_coord = Coord4D(x, y, 0, 0)
                if value == "#":
                    active_cells.add(new_coord)

        ints = {-1, 0, 1}
        neighbor_references = {Coord4D(x, y, z, w) for x in ints for y in ints for z in ints for w in ints
                               if not (x, y, z, w) == (0, 0, 0, 0)}
        return PowerGrid4D(active_cells=active_cells, neighbor_references=neighbor_references)


if __name__ == '__main__':
    # test_grid = PowerGrid.parse_data(TEST_DATA)
    # test_grid.run_cycles(6)
    # test_grid_p2 = PowerGrid4D.parse_data(TEST_DATA)
    # test_grid_p2.run_cycles(6)

    # true_grid = PowerGrid.parse_data(CHALLENGE_DATA)
    # true_grid.run_cycles(6)
    true_grid = PowerGrid4D.parse_data(CHALLENGE_DATA)
    true_grid.run_cycles(6)
