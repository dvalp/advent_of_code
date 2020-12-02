import re
from collections import Counter
from typing import Callable


def validate_password(line: str) -> bool:
    lower, upper, letter, _, pwd = re.split("[-: ]", line)
    return int(lower) <= Counter(pwd)[letter] <= int(upper)


def validate_again(line: str) -> bool:
    pos1, pos2, letter, _, pwd = re.split("[-: ]", line)
    first = pwd[int(pos1) - 1] == letter
    second = pwd[int(pos2) - 1] == letter
    return first ^ second


def count_valid_passwords(func: Callable) -> int:
    with open("data/input_day02.txt", "r") as f:
        return sum(func(line) for line in f)


if __name__ == '__main__':
    print(count_valid_passwords(validate_password))
    print(count_valid_passwords(validate_again))
