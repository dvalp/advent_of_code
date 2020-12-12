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
    move_type: Literal["normal", "waypoint"] = "normal"

    @property
    def manhattan_dist(self) -> int:
        return abs(self.ship_lat) + abs(self.ship_long)

    def read_instructions(self, instructions: list[str]) -> None:
        if self.move_type == "normal":
            move_function = self.move_direction
            turn_function = self.change_direction
        else:
            move_function = self.move_waypoint
            turn_function = self.rotate_waypoint

        for line in instructions:
            command, value = line[0], int(line[1:])
            if command in set("NESWF"):
                move_function(command, value)
            elif command in set("LR"):
                turn_function(command, value)

    def move_direction(self, command: str, dist: int, wp: bool = False) -> None:
        direction = self.facing if command == "F" else Direction[command]
        dist = -dist if direction in {Direction.W, Direction.S} else dist
        if wp:
            lat_field, long_field = "wp_lat", "wp_long"
            lat, long = self.wp_lat, self.wp_long
        else:
            lat_field, long_field = "ship_lat", "ship_long"
            lat, long = self.ship_lat, self.ship_long

        if direction in {Direction.E, Direction.W}:
            self.__setattr__(lat_field, lat + dist)
        elif direction in {Direction.N, Direction.S}:
            self.__setattr__(long_field, long + dist)
        else:
            raise ValueError("self.facing only has 4 allowed values. %s is invalid." % direction)

    def change_direction(self, command: str, value: int) -> None:
        degrees = self.facing.value
        if command == "L":
            degrees = (degrees + 360 - value) % 360
        elif command == "R":
            degrees = (degrees + value) % 360
        else:
            raise ValueError("Ship can only turn L or R")
        self.facing = Direction(degrees)

    def move_waypoint(self, command: str, dist: int):
        if command == "F":
            self.ship_lat += dist * self.wp_lat
            self.ship_long += dist * self.wp_long
        else:
            self.move_direction(command, dist, wp=True)

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
""".split()
    full_instructions = Path("../data/input_day12.txt").read_text().split()
    nav = Navigator()
    nav.read_instructions(sample_directions)
    print(nav.manhattan_dist)

    nav_complete = Navigator()
    nav_complete.read_instructions(full_instructions)
    print(nav_complete.manhattan_dist)

    nav_complete = Navigator(move_type="waypoint")
    nav_complete.read_instructions(sample_directions)
    print(nav_complete.manhattan_dist)

    nav_complete = Navigator(move_type="waypoint")
    nav_complete.read_instructions(full_instructions)
    print(nav_complete.manhattan_dist)
