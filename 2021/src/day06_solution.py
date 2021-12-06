from pathlib import Path

import numpy as np

RAW = [int(val) for val in "3,4,3,1,2".split(",")]


def calculate_population(input_data: list[int], iterations: int):
    data = np.array(input_data)
    for _ in range(iterations):
        data -= 1
        if breeder_count := np.count_nonzero(data == -1):
            data = np.append(data, [8] * breeder_count)
        data[data == -1] = 6

    return len(data)


def solve(fish_ages: list[int], days: int) -> int:
    """
    My solution was useless for the larger number of days
    I really like the modulo approach from this python solution
    https://github.com/Peter200lx/advent-of-code/blob/master/2021/day06.py
    """
    count_of_fish_in_age = [fish_ages.count(i) for i in range(9)]
    for i in range(days):
        count_of_fish_in_age[(i + 7) % 9] += count_of_fish_in_age[i % 9]
    return sum(count_of_fish_in_age)


if __name__ == '__main__':
    file_input = [int(val) for val in Path("../data/input_day06.txt").read_text().strip().split(",")]
    print(calculate_population(RAW, 18))
    print(calculate_population(file_input, 80))
    print(calculate_population(RAW, 256))
    print(calculate_population(file_input, 256))
