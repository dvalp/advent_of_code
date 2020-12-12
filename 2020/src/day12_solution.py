from dataclasses import dataclass
from enum import IntEnum


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
        for line in instructions:
            command, value = line[0], int(line[1:])
            if command == "F":
                self.move_direction(self.facing, value)
            elif command in set("NESW"):
                dirs = {"N": Direction.N, "E": Direction.E, "S": Direction.S, "W": Direction.W}
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
            raise ValueError("slef.facing only has 4 allowed vallues. %s is invalid." % self.facing)

    def change_direction(self, command: str, value: int) -> None:
        degrees = self.facing
        if command == "L":
            degrees = abs(degrees - value) % 360
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