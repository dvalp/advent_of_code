from collections import deque
from copy import deepcopy
from pathlib import Path
from typing import NamedTuple, Optional


class Instruction(NamedTuple):
    count: int
    origin: int
    destination: int


def restack_crates(moves: list[str], arrangement: dict[int, deque[str]], batch_move: Optional[bool] = False) -> str:
    for line in moves:
        inst = Instruction(*[int(val) for val in line.split()[1::2]])
        crate_stack = [arrangement[inst.origin].pop() for _ in range(inst.count)]
        crate_stack = reversed(crate_stack) if batch_move else crate_stack
        arrangement[inst.destination].extend(crate_stack)
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
    print(restack_crates(file_data, deepcopy(original_stacks), batch_move=True))
