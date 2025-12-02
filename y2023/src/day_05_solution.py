from collections import defaultdict, namedtuple
from pathlib import Path

ResultValues = namedtuple("ResultValues", "points counts")


def get_location_from_seed(almanac):
    seed_conversions = {}
    for section in almanac:
        name, values = section.split(":")
        seed_conversions[name] = [row.split() for row in values.strip().splitlines()]

    for conversions in seed_conversions["seed-to-soil"]:



if __name__ == '__main__':
    file_data = Path("y2023/data/input_day04.txt").read_text().strip().split("\n\n")
    print(get_location_from_seed(file_data))
