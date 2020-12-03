import math
from typing import Iterable


def tree_count():
    horiz = 0

    with open("data/input_day03.txt", "r") as f:
        next(f)
        for line in f:
            horiz += 3
            yield line[horiz % 31] == '#'


def tree_count_deluxe(
        tree_map: list[str],
        start_coords: tuple[int, int] = (0, 0),
        offsets: tuple[int, int] = (1, 1)
) -> Iterable[bool]:
    horiz_offset, vert_offset = offsets
    vert, horiz = start_coords
    width = len(tree_map[0])
    while vert < len(tree_map):
        yield tree_map[vert][horiz % width] == "#"
        horiz += horiz_offset
        vert += vert_offset


def check_all_slopes(tree_map: list[str]) -> int:
    route_offsets = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod(sum(tree_count_deluxe(tree_map=tree_map, offsets=offsets)) for offsets in route_offsets)


def parse_input(fpath="data/input_day03.txt") -> list[str]:
    with open(fpath, "r") as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    print(sum(tree_count()))
    t_map = """..##.......\n
    #...#...#..\n
    .#....#..#.\n
    ..#.#...#.#\n
    .#...##..#.\n
    ..#.##.....\n
    .#.#.#....#\n
    .#........#\n
    #.##...#...\n
    #...##....#\n
    .#..#...#.#\n""".split()
    print(check_all_slopes(t_map))
    print(sum(tree_count_deluxe(tree_map=parse_input(), offsets=(3, 1))))
    print(check_all_slopes(parse_input()))
