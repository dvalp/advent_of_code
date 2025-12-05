import numpy as np
import pytest

from y2025.src.day_04_solution import convert_data, count_roles


@pytest.fixture
def sample_input():
    return """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def test_count_roles(sample_input):
    result = count_roles(sample_input)
    assert result == 13


def test_convert_data(sample_input):
    result = convert_data(sample_input)
    expected = np.array(
        [[0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
         [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
         [1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
         [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
         [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
         [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
         [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0]]
    )
    assert (result == expected).all()
