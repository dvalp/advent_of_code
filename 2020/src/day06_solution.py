from collections import Counter
from pathlib import Path
from typing import Callable


def total_answers(func: Callable) -> int:
    fpath = Path("../data/input_day06.txt")
    answers = fpath.read_text().split("\n\n")
    return sum(func(answer) for answer in answers)


def count_group(answer: str) -> int:
    """Count answers by anyone in the group"""
    return len(set(answer.replace("\n", "")))


def count_group_yes(answer: str) -> int:
    """Count only answers given by all members of the group"""
    group_size = len(answer.split())
    counts = Counter(answer.replace("\n", ""))
    return sum(True for val in counts.values() if val == group_size)


# Using sets better
def answers_with_sets():
    fpath = Path("../data/input_day06.txt")
    groups = [[set(person) for person in group.split()] for group in fpath.read_text().split("\n\n")]
    any_answered = (sum(len(set.union(*group)) for group in groups))
    all_answered = (sum(len(set.intersection(*group)) for group in groups))
    return any_answered, all_answered


if __name__ == '__main__':
    print(total_answers(count_group))
    print(total_answers(count_group_yes))
    print(answers_with_sets())
