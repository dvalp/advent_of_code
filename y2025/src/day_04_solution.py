import numpy as np
from scipy import signal
from pathlib import Path

char_translation = str.maketrans(".@", "01")


def convert_data(roll_map: str) -> np.array:
    """
    Convert roll map string to numpy array.

    Args:
        roll_map: Map where `.` represents empty space and `@` represents a
            roll.

    Returns:
        Numpy array representation of the roll map.
    """
    input_lines = roll_map.translate(char_translation).splitlines()
    return np.array([list(line) for line in input_lines], dtype=int)


def count_roles(roll_map: str) -> int:
    """
    Analyze map of rolls to find which roles can be moved.

    A roll can be moved only if it has fewer than 4 rolls in the surrounding
    space. This can be calculated using convolutions to sum the rolls found in
    the surrounding spaces.

    Args:
        roll_map: Map where `.` represents empty space and `@` represents a
            roll.

    Returns:
        Sum of rolls that can be moved.
    """
    roll_map = convert_data(roll_map)
    kernel = np.array([[1,1,1],[1,0,1],[1,1,1]], dtype="int8")
    convolve_map = signal.convolve2d(roll_map, kernel, mode="same")
    movable_rolls = np.logical_and(roll_map == 1, convolve_map < 4)
    return np.sum(movable_rolls)


if __name__ == "__main__":
    file_data = Path("y2025/data/input_day_04.txt").read_text().strip()
    result = count_roles(file_data)
    print(f"Part 1: {result}")