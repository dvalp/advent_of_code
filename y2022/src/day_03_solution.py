import string
from itertools import islice
from pathlib import Path


def inspect_packing(data: list[str]) -> int:
    total = 0
    for line in data:
        split_point = len(line) // 2
        pack_1 = set(line[:split_point])
        pack_2 = set(line[split_point:])
        duplicate = next(iter(pack_1 & pack_2))
        total += string.ascii_letters.index(duplicate) + 1
    return total


def find_badges(data: list[str]) -> int:
    total = 0
    it = iter(data)
    while group := list(islice(it, 3)):
        sets = [set(pack) for pack in group]
        badge = next(iter(sets[0].intersection(*sets[1:])))
        total += string.ascii_letters.index(badge) + 1
    return total


if __name__ == '__main__':
    file_data = Path("../data/input_day_03.txt").read_text().strip().split("\n")
    print(inspect_packing(file_data))
    print(find_badges(file_data))
