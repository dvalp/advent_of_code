from enum import IntEnum
from pathlib import Path


class Score(IntEnum):
    LOSE = 0
    DRAW = 3
    WIN = 6
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def solve_games(data: list[str], scoring: dict[str, dict[str, Score]]) -> int:
    total = 0
    for line in data:
        first, second = line.split()
        total += scoring[second]["score"] + scoring[second][first]
    return total


def first_game(data: list[str]) -> int:
    scoring = {
        "X": {"score": Score.ROCK, "A": Score.DRAW, "B": Score.LOSE, "C": Score.WIN},
        "Y": {"score": Score.PAPER, "A": Score.WIN, "B": Score.DRAW, "C": Score.LOSE},
        "Z": {"score": Score.SCISSORS, "A": Score.LOSE, "B": Score.WIN, "C": Score.DRAW}
    }
    return solve_games(data, scoring)


def second_game(data: list[str]) -> int:
    scoring = {
        "X": {"score": Score.LOSE, "A": Score.SCISSORS, "B": Score.ROCK, "C": Score.PAPER},
        "Y": {"score": Score.DRAW, "A": Score.ROCK, "B": Score.PAPER, "C": Score.SCISSORS},
        "Z": {"score": Score.WIN, "A": Score.PAPER, "B": Score.SCISSORS, "C": Score.ROCK}
    }
    return solve_games(data, scoring)


if __name__ == '__main__':
    file_data = Path("../data/input_day_02.txt").read_text().strip().split("\n")
    print(first_game(file_data))
    print(second_game(file_data))
