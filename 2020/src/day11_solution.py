from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import NamedTuple


class State(Enum):
    EMPTY = 0
    FILLED = 1
    FLOOR = None


class Action(Enum):
    FILL = 0
    EMPTY = 4


class Point(NamedTuple):
    row: int
    column: int


@dataclass
class Seat:
    location: Point
    status: State


@dataclass
class Board:
    seat_map: dict[Point, State]

    @staticmethod
    def initialize_board(empty_map: str):
        """All seats start empty, so populate the dictionary with only empty seats"""
        new_map = {}
        current_location = Point(0, 0)
        for c in empty_map:
            if c == "\n":
                current_location = Point(current_location.row + 1, 0)
            if c == "L":
                new_map[current_location] = State.EMPTY
                current_location = Point(current_location.row, current_location.column + 1)
        return Board(new_map)

    def update_board(self):
        pass


if __name__ == '__main__':
    sample_map = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    challenge_map = Path("../data/input_day11.txt").read_text()
    sample_board = Board.initialize_board(sample_map)
