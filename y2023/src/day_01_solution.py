from enum import StrEnum
from pathlib import Path


class Number(StrEnum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    ZERO = "0"


def calibration_total(calibrations: list[str]) -> int:
    total = 0
    for line in calibrations:
        digits = [c for c in line if c.isdigit()]
        total += int("".join([digits[0], digits[-1]]))
    return total


def calibration_total_corrected(calibrations: list[str]) -> int:
    total = 0
    for line in calibrations:
        digits = []
        for i in range(len(line)):
            for key, value in Number.__members__.items():
                if line[i:].startswith(key.lower()):
                    digits.append(str(value))
                elif (char := line[i]).isdigit():
                    digits.append(char)
                    break
        total += int("".join([digits[0], digits[-1]]))
    return total


if __name__ == '__main__':
    file_data = Path("y2023/data/input_day01.txt").read_text().strip().splitlines()
    print(calibration_total(file_data))
    print(calibration_total_corrected(file_data))
