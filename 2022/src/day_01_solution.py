from pathlib import Path
from typing import Iterable

SAMPLE = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".strip().split("\n")


def get_calorie_values(data: Iterable = None, count=1) -> int:
    if data is None:
        data = SAMPLE
    totals = []
    calories = 0
    for line in data:
        if line:
            calories += int(line)
        else:
            totals.append(calories)
            calories = 0
    else:
        totals.append(calories)

    return sum(sorted(totals)[count * -1:])


if __name__ == '__main__':
    print(get_calorie_values())
    file_data = Path("../data/input_day_01.txt").read_text().strip().split("\n")
    print(get_calorie_values(file_data))
    print(get_calorie_values(file_data, 3))
