import pytest
from y2023.src.day_01_solution import calibration_total, calibration_total_corrected

@pytest.fixture
def calibrations():
    return """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".strip().splitlines()


@pytest.fixture
def additional_calibrations():
    return """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".strip().splitlines()


def test_calibration_total(calibrations):
    assert calibration_total(calibrations) == 142


def test_calibration_total_corrected(additional_calibrations):
    assert calibration_total_corrected(additional_calibrations) == 281
