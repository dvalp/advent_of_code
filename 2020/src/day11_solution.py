from dataclasses import dataclass
from enum import IntEnum
from itertools import product
from pathlib import Path
from typing import NamedTuple


class State(IntEnum):
    EMPTY = 0
    FILLED = 1
    FLOOR = -1


class Action(IntEnum):
    FILL = 0
    EMPTY = 4


class Point(NamedTuple):
    row: int
    column: int


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

    def count_neighbors(self, seat_position: Point):
        rows = range(seat_position.row - 1, seat_position.row + 2)
        columns = range(seat_position.column - 1, seat_position.column + 2)
        search_space = {Point(*coord) for coord in product(rows, columns) if coord != seat_position}
        return sum(self.seat_map.get(neighbor, State.EMPTY) for neighbor in search_space)

    def update_board(self):
        new_map = dict()
        for seat in self.seat_map:
            number_neighbors = self.count_neighbors(seat)
            if number_neighbors == Action.FILL:
                new_map[seat] = State.FILLED
            if number_neighbors >= Action.EMPTY:
                new_map[seat] = State.EMPTY
        return Board(new_map)


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
    print(sample_board.count_neighbors(Point(0, 2)))
    print(sample_board)
    print(sample_board.update_board())
    print(sum(sample_board.update_board().seat_map.values()))
