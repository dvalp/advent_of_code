from collections import deque
from copy import deepcopy
from pathlib import Path
from typing import NamedTuple


class Instruction(NamedTuple):
    count: int
    origin: int
    destination: int


def restack_crates(moves: list[str], arrangement: dict[int, deque[str]]) -> str:
    for line in moves:
        inst = Instruction(*[int(val) for val in line.split()[1::2]])
        for _ in range(inst.count):
            arrangement[inst.destination].append(arrangement[inst.origin].pop())
    return "".join(stack[-1] for stack in arrangement.values())


def restack_crates_upgrade(moves: list[str], arrangement: dict[int, deque[str]]) -> str:
    for line in moves:
        inst = Instruction(*[int(val) for val in line.split()[1::2]])
        crate_stack = [arrangement[inst.origin].pop() for _ in range(inst.count)]
        arrangement[inst.destination].extend(reversed(crate_stack))
    return "".join(stack[-1] for stack in arrangement.values())


if __name__ == '__main__':
    original_stacks = {
        1: deque("RGJBTVZ"),
        2: deque("JRVL"),
        3: deque("SQF"),
        4: deque("ZHNLFVQG"),
        5: deque("RQTJCSMW"),
        6: deque("SWTCHF"),
        7: deque("DZCVFNJ"),
        8: deque("LGZDWRFQ"),
        9: deque("JBWVP"),
    }
    file_data = Path("../data/input_day_05.1.txt").read_text().strip().splitlines()
    print(restack_crates(file_data, deepcopy(original_stacks)))
    print(restack_crates_upgrade(file_data, deepcopy(original_stacks)))
