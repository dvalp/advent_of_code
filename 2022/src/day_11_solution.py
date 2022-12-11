import math
import operator
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, TypeAlias, Iterable

math_operator: TypeAlias = Callable[[int, int], int]
@dataclass
class Monkey:
    name: str
    operation: math_operator
    operation_value: int
    test_value: int
    true_target: int
    false_target: int
    items: deque[int]
    inspection_count: int = 0


class MonkeyRunner:
    operators: dict[str, math_operator] = {
        "+": operator.add,
        "*": operator.mul,
        "**": operator.pow
    }

    def __init__(self, monkey_data: list[str], rounds=20, worry_level_divider=3):
        self.monkeys = dict(self.parse_data(monkey_data))
        self.modulus = math.lcm(*[monkey.test_value for monkey in self.monkeys.values()])
        self.rounds = rounds
        self.worry_level_divider = worry_level_divider

    def parse_data(self, monkey_data: list[str]) -> Iterable[tuple[int, Monkey]]:
        for info in monkey_data:
            lines = info.splitlines()
            name = lines[0].replace(":", "").strip()
            op, opval = lines[2].split()[-2:]
            if opval == "old" and op == "*":
                opval = 2
                op = "**"
            yield (int(name.split()[-1]),
                   Monkey(
                       name=name,
                       items=deque(int(item) for item in lines[1].replace(",", "").split() if item.isdigit()),
                       operation=self.operators[op],
                       operation_value=int(opval),
                       test_value=int(lines[3].split()[-1]),
                       true_target=int(lines[4].split()[-1]),
                       false_target=int(lines[5].split()[-1]),
                   ))

    def run_turn(self, monkey: Monkey):
        while monkey.items:
            item = monkey.items.popleft()
            monkey.inspection_count += 1
            item = monkey.operation(item, monkey.operation_value) // self.worry_level_divider
            item %= self.modulus
            pass_to = monkey.true_target if (item % monkey.test_value == 0) else monkey.false_target
            self.monkeys[pass_to].items.append(item)

    def run_rounds(self):
        for round_number in range(self.rounds):
            for monkey in self.monkeys.values():
                self.run_turn(monkey)

    def evaluate_monkey_business(self) -> int:
        val1, val2 = sorted(monkey.inspection_count for monkey in self.monkeys.values())[-2:]
        return val1 * val2


if __name__ == '__main__':
    file_data = Path("../data/input_day_11.txt").read_text().strip().split("\n\n")
    runner = MonkeyRunner(file_data)
    runner.run_rounds()
    print(runner.evaluate_monkey_business())

    runner = MonkeyRunner(file_data, rounds=10_000, worry_level_divider=1)
    runner.run_rounds()
    print(runner.evaluate_monkey_business())
