import math
from pathlib import Path
from enum import IntEnum


class CubeCount(IntEnum):
    RED = 12
    GREEN = 13
    BLUE = 14


def game_validator(games: list[str]) -> int:
    game_total = 0
    for game in games:
        parts = game.split(":")
        game_id = int(parts[0].split()[1])
        game_results = []

        for sample in parts[1].split(";"):
            counts = dict((color.split())[::-1] for color in sample.split(", "))
            game_results.append(all((int(value) <= CubeCount[key.upper()]) for key, value in counts.items()))

        if all(game_results):
            game_total += game_id

    return game_total


def game_minimum(games: list[str]) -> int:
    game_sum = 0
    for game in games:
        parts = game.split(":")
        max_counts = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for sample in parts[1].split(";"):
            counts = dict((color.split())[::-1] for color in sample.split(", "))
            for key, value in counts.items():
                if int(value) > max_counts[key]:
                    max_counts[key] = int(value)

        game_sum += math.prod(max_counts.values())

    return game_sum


if __name__ == '__main__':
    file_data = Path("y2023/data/input_day02.txt").read_text().strip().splitlines()
    print(game_validator(file_data))
    print(game_minimum(file_data))
