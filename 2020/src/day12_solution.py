from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path


class Direction(IntEnum):
    N = 0
    E = 90
    S = 180
    W = 270


@dataclass
class Navigator:
    long_dist: int = 0
    lat_dist: int = 0
    facing: IntEnum = Direction.E

    def read_instructions(self, instructions: list[str]) -> None:
        dirs = {"N": Direction.N, "E": Direction.E, "S": Direction.S, "W": Direction.W}
        for line in instructions:
            command, value = line[0], int(line[1:])
            if command == "F":
                self.move_direction(self.facing, value)
            elif command in set("NESW"):
                self.move_direction(dirs[command], value)
            elif command in set("LR"):
                self.change_direction(command, value)

    def move_direction(self, direction: IntEnum, dist: int) -> None:
        if direction == Direction.E:
            self.lat_dist += dist
        elif direction == Direction.N:
            self.long_dist += dist
        elif direction == Direction.W:
            self.lat_dist -= dist
        elif direction == Direction.S:
            self.long_dist -= dist
        else:
            raise ValueError("slef.facing only has 4 allowed vallues. %s is invalid." % direction)

    def change_direction(self, command: str, value: int) -> None:
        degrees = self.facing.value
        if command == "L":
            degrees = (degrees + 360 - value) % 360
        elif command == "R":
            degrees = (degrees + value) % 360
        else:
            raise ValueError("Ship can only turn L or R")
        self.facing = Direction(degrees)

    @property
    def manhattan_dist(self) -> int:
        return abs(self.lat_dist) + abs(self.long_dist)


if __name__ == '__main__':
    sample_directions = """F10
N3
F7
R90
F11
"""
    full_instructions = Path("../data/input_day12.txt").read_text().split()
    nav = Navigator()
    nav.read_instructions(sample_directions.split())
    print(nav.manhattan_dist)

    nav_complete = Navigator()
    nav_complete.read_instructions(full_instructions)
    print(nav_complete.manhattan_dist)
