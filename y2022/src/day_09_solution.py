from __future__ import annotations
from dataclasses import dataclass, astuple
import math
from pathlib import Path


@dataclass(eq=True)
class Point:
    x: int
    y: int

    def __add__(self, other: Point):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    @staticmethod
    def calculate_move(difference: Point):
        x = -1 if difference.x < 0 else math.ceil(abs(difference.x) / 2)
        y = -1 if difference.y < 0 else math.ceil(abs(difference.y) / 2)
        return Point(x, y)


MOVES = {
    "L": Point(-1, 0),
    "R": Point(1, 0),
    "U": Point(0, 1),
    "D": Point(0, -1),
}


def track_path(moves):
    head, tail = Point(0, 0), Point(0, 0)
    tail_locations = {astuple(tail)}
    for instruction in moves:
        direction, distance = instruction.split()
        for _ in range(int(distance)):
            head += MOVES[direction]
            difference = astuple(head - tail)
            if any(abs(val) >= 2 for val in difference):
                tail = head - MOVES[direction]
                tail_locations.add(astuple(tail))
    return len(tail_locations)


def track_path2(moves, tail_len):
    head, tail = Point(0, 0), Point(0, 0)
    segments = [Point(0, 0) for _ in range(tail_len - 2)]
    tail_locations = {astuple(tail)}
    for instruction in moves:
        direction, distance = instruction.split()
        for _ in range(int(distance)):
            head += MOVES[direction]
            previous = head
            for segment in segments:
                difference = previous - segment
                if abs(difference.x) >= 2 or abs(difference.y) >= 2:
                    segment += segment.calculate_move(difference)
                previous = segment
            difference = previous - tail
            if abs(difference.x) >= 2 or abs(difference.y) >= 2:
                tail += tail.calculate_move(difference)
                tail_locations.add(astuple(tail))

    return len(tail_locations)


if __name__ == '__main__':
    file_data = Path("../data/input_day_09.txt").read_text().strip().splitlines()
    print(track_path(file_data))
    print(track_path2(file_data, 10))
