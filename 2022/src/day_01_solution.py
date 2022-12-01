from pathlib import Path
from typing import Iterable


def get_calorie_values(data: Iterable = None, count=1) -> int:
    totals = []
    calories = 0
    for line in data:
        if value := line.strip():
            calories += int(value)
        else:
            totals.append(calories)
            calories = 0
    else:
        totals.append(calories)

    return sum(sorted(totals)[count * -1:])


if __name__ == '__main__':
    file_data = Path("../data/input_day_01.txt").read_text().strip().split("\n")
    print(get_calorie_values(file_data))
    print(get_calorie_values(file_data, 3))
