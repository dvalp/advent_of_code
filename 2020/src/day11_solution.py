from dataclasses import dataclass
from enum import Enum


class State(Enum):
    EMPTY = "L"
    FILLED = "#"
    FLOOR = "."


class Action(Enum):
    FILL = 0
    EMPTY = 4


@dataclass
class Seat:
    value: State
    row: int
    column: int


@dataclass
class Board:
    map: list[list[str]]

    def initialize_board(self):
        pass

    def update_board(self):
        pass
