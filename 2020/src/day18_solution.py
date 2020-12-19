import math
import re
from pathlib import Path
from typing import Callable

EXAMPLES = [
    ("1 + 2 * 3 + 4 * 5 + 6", 71),
    ("1 + (2 * 3) + (4 * (5 + 6))", 51),
    ("2 * 3 + (4 * 5)", 26),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
]
EXAMPLES2 = [
    ("1 + 2 * 3 + 4 * 5 + 6", 231),
    ("1 + (2 * 3) + (4 * (5 + 6))", 51),
    ("2 * 3 + (4 * 5)", 46),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),
]

PARENS = re.compile(r"\([^(]+?\)")
ADDITION = re.compile(r"\d+ \+ \d+")


def do_math(formula: list[str]) -> int:
    total = int(formula[0])
    for idx in range(1, len(formula), 2):
        op = formula[idx]
        if op == "*":
            total *= int(formula[idx + 1])
        elif op == "+":
            total += int(formula[idx + 1])
        else:
            raise ValueError("Unexpected op: %s" % op)
    return total


def evaluate_formula(input_text: str) -> int:
    while match := re.search(PARENS, input_text):
        result = do_math(match.group()[1:-1].split())
        input_text = input_text.replace(match.group(), str(result))
    else:
        return do_math(input_text.split())


def evaluate_formula2(input_text: str) -> int:
    while match := re.search(PARENS, input_text):
        result = do_stupid_math(match.group()[1:-1])
        input_text = input_text.replace(match.group(), str(result))
    else:
        return do_stupid_math(input_text)


def do_stupid_math(input_text: str) -> int:
    while match := re.search(ADDITION, input_text):
        result = sum(int(val) for val in match.group().split(" + "))
        input_text = input_text.replace(match.group(), str(result))
    else:
        return math.prod(int(val) for val in input_text.split(" * "))


if __name__ == '__main__':
    # for text, expected in EXAMPLES:
    #     print(evaluate_formula(text), expected)
    for text, expected in EXAMPLES2:
        print(evaluate_formula2(text), expected)

    challenge_text = Path("../data/input_day18.txt").read_text().strip().split("\n")
    # print(sum(evaluate_formula(line) for line in challenge_text))
    print(sum(evaluate_formula2(line) for line in challenge_text))
