from collections import deque
from pathlib import Path

SAMPLE_DATA = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".strip().split("\n")


def chunk_validation(input_data: list[str]) -> tuple[int, int]:
    open_stack = deque()
    error_score = 0
    error_values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    completion_scores = []
    completion_values = {"(": 1, "[": 2, "{": 3, "<": 4}

    for line in input_data:
        for c in line:
            if c in set("([{<"):
                open_stack.append(c)
            else:
                match (open_stack.pop(), c):
                    case ("(", ")") | ("[", "]") | ("{", "}") | ("<", ">"):
                        continue
                    case _:
                        error_score += error_values[c]
                        open_stack = deque()
                break
        if open_stack:
            current_score = 0
            while open_stack:
                current_score *= 5
                current_score += completion_values[open_stack.pop()]
            completion_scores.append(current_score)
    middle_score = sorted(completion_scores)[len(completion_scores) // 2]
    return error_score, middle_score


if __name__ == '__main__':
    file_data = Path("../data/input_day10.txt").read_text().strip().split("\n")
    print(chunk_validation(SAMPLE_DATA))
    print(chunk_validation(file_data))
