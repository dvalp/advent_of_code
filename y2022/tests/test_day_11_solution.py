import pytest
from src.day_11_solution import MonkeyRunner


@pytest.fixture
def monkey_list():
    return """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split("\n\n")


def test_monkey_runner(monkey_list):
    runner = MonkeyRunner(monkey_list)
    runner.run_rounds()
    assert runner.evaluate_monkey_business() == 10605


def test_monkey_runner_high_worry(monkey_list):
    runner = MonkeyRunner(monkey_list, rounds=10_000, worry_level_divider=1)
    runner.run_rounds()
    assert runner.evaluate_monkey_business() == 2713310158
