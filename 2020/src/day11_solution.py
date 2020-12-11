from dataclasses import dataclass
from enum import IntEnum
from itertools import product, repeat
from pathlib import Path
from typing import NamedTuple, Literal


class State(IntEnum):
    EMPTY = 0
    FILLED = 1
    FLOOR = -1


class Point(NamedTuple):
    row: int
    column: int


@dataclass
class Board:
    seat_map: dict[Point, State]
    max_neighbors: int
    n_rows: int
    n_columns: int
    count_function: Literal["adj", "vis"] = "adj"

    @property
    def filled_seat_count(self):
        return sum(self.seat_map.values())

    @property
    def number_of_seats(self):
        return len(self.seat_map)

    @staticmethod
    def initialize_board(empty_map: str, threshold: int, count_function: Literal["adj", "vis"] = "adj"):
        """All seats start empty, so populate the dictionary with only empty seats"""
        n_rows = empty_map.count("\n")
        n_columns = empty_map.find("\n")
        new_map = {}
        current_location = Point(0, 0)

        for c in empty_map:
            if c == "\n":
                current_location = Point(current_location.row + 1, 0)
                continue
            elif c == "L":
                new_map[current_location] = State.EMPTY
            current_location = Point(current_location.row, current_location.column + 1)
        return Board(new_map, max_neighbors=threshold, n_rows=n_rows, n_columns=n_columns,
                     count_function=count_function)

    def count_adjacent_neighbors(self, seat_position: Point):
        rows = range(seat_position.row - 1, seat_position.row + 2)
        columns = range(seat_position.column - 1, seat_position.column + 2)
        search_space = {Point(*coord) for coord in product(rows, columns) if coord != seat_position}
        return sum(self.seat_map.get(neighbor, State.EMPTY) for neighbor in search_space)

    def count_visible_neighbors(self, seat_position: Point) -> int:
        row_lower = list(range(seat_position.row - 1, -1, -1))
        row_higher = list(range(seat_position.row + 1, self.n_rows))
        column_lower = list(range(seat_position.column - 1, -1, -1))
        column_higher = list(range(seat_position.column + 1, self.n_columns))
        neighbor_count = 0
        search_directions = [
            zip(repeat(seat_position.row), column_lower),
            zip(repeat(seat_position.row), column_higher),
            zip(row_lower, repeat(seat_position.column)),
            zip(row_higher, repeat(seat_position.column)),
            zip(row_lower, column_lower),
            zip(row_lower, column_higher),
            zip(row_higher, column_lower),
            zip(row_higher, column_higher)
        ]
        for direction in search_directions:
            for position in direction:
                if position in self.seat_map:
                    neighbor_count += self.seat_map[Point(*position)]
                    break

            if neighbor_count >= self.max_neighbors:
                break

        return neighbor_count

    def update_board(self):
        new_map = dict()

        if self.count_function == "adj":
            count_neighbors = self.count_adjacent_neighbors
        elif self.count_function == "vis":
            count_neighbors = self.count_visible_neighbors
        else:
            raise ValueError("Only allowed values for search functions are 'adj' or 'vis'")

        for seat in self.seat_map:
            number_neighbors = count_neighbors(seat)
            if number_neighbors == 0:
                new_map[seat] = State.FILLED
            elif number_neighbors >= self.max_neighbors:
                new_map[seat] = State.EMPTY
            else:
                new_map[seat] = self.seat_map[seat]
        return new_map

    def find_stable_state(self):
        while True:
            new_map = self.update_board()

            if new_map == self.seat_map:
                return self.filled_seat_count

            self.seat_map = new_map


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
L.LLLLL.LL
"""
    challenge_map = Path("../data/input_day11.txt").read_text()

    sample_board = Board.initialize_board(sample_map, 4)
    sample_board_p2 = Board.initialize_board(sample_map, 5, "vis")
    challenge_board = Board.initialize_board(challenge_map, 4)
    challenge_board_p2 = Board.initialize_board(challenge_map, 5, "vis")

    # print(sample_board.count_neighbors(Point(0, 2)))
    # print(sample_board)
    # print(sample_board.update_board())
    # print(sample_board.find_stable_state())
    print(sample_board_p2.find_stable_state())
    print(challenge_board_p2.find_stable_state())
    #
    # print(challenge_board.find_stable_state())
    # sample_board.seat_map = sample_board.update_board()
    # print(sample_board_p2.count_visible_neighbors(Point(row=4, column=3)))
