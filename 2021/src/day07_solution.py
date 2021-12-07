import numpy as np
from pathlib import Path


def calculate_fuel(input_data: np.array) -> np.ndarray:
    return np.sum(np.abs(input_data - int(np.median(input_data))))


def calculate_increased_fuel(input_data: np.array) -> int:
    min_cost = np.iinfo(np.int64).max
    for position in range(input_data.min(), input_data.max()):
        new_cost = sum((num * (num + 1) // 2) for num in np.abs(input_data - position))
        if new_cost > min_cost:
            return min_cost
        min_cost = min(min_cost, new_cost)


if __name__ == '__main__':
    sample_input = np.array([int(value) for value in "16,1,2,0,4,2,7,1,2,14".split(",")])
    file_input = np.array([int(val) for val in Path("../data/input_day07.txt").read_text().strip().split(",")])
    print(calculate_increased_fuel(file_input))
