from collections import Counter
from pathlib import Path
from typing import Callable


def total_answers(func: Callable):
    fpath = Path("../data/input_day06.txt")
    answers = fpath.read_text().split("\n\n")
    return sum(func(answer) for answer in answers)


def count_group(answer):
    return len(set(answer.replace("\n", "")))


def count_group_yes(answer):
    group_size = len(answer.split())
    counts = Counter(answer.replace("\n", ""))
    return sum(True for val in counts.values() if val == group_size)


if __name__ == '__main__':
    print(total_answers(count_group))
    print(total_answers(count_group_yes))