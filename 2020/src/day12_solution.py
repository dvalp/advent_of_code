from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path
from typing import Literal


class Direction(IntEnum):
    N = 0
    E = 90
    S = 180
    W = 270


@dataclass
class Navigator:
    ship_long: int = 0
    ship_lat: int = 0
    wp_lat: int = 10
    wp_long: int = 1
    facing: IntEnum = Direction.E

    @property
    def manhattan_dist(self) -> int:
        return abs(self.ship_lat) + abs(self.ship_long)

    def read_instructions(self, instructions: list[str], move: Literal["normal", "waypoint"] = "normal") -> None:
        dirs = {"N": Direction.N, "E": Direction.E, "S": Direction.S, "W": Direction.W}
        if move == "normal":
            move_function = self.move_direction
            turn_function = self.change_direction
        else:
            move_function = self.move_waypoint
            turn_function = self.rotate_waypoint

        for line in instructions:
            command, value = line[0], int(line[1:])
            if command == "F":
                move_function(direction=self.facing, dist=value)
            elif command in set("NESW"):
                move_function(dirs[command], value)
            elif command in set("LR"):
                turn_function(command, value)

    def move_direction(self, direction: IntEnum, dist: int) -> None:
        if direction == Direction.E:
            self.ship_lat += dist
        elif direction == Direction.N:
            self.ship_long += dist
        elif direction == Direction.W:
            self.ship_lat -= dist
        elif direction == Direction.S:
            self.ship_long -= dist
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

    def move_waypoint(self, direction: IntEnum, dist: int):
        pass

    def rotate_waypoint(self, command: str, value: int):
        if (command == "L" and value == 90) or (command == "R" and value == 270):
            self.wp_lat, self.wp_long = -self.wp_long, self.wp_lat
        elif (command == "R" and value == 90) or (command == "L" and value == 270):
            self.wp_lat, self.wp_long = self.wp_long, -self.wp_lat
        elif value == 180:
            self.wp_lat, self.wp_long = -self.wp_lat, -self.wp_long
        else:
            raise ValueError("Turn instruction or value was invalid")


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
