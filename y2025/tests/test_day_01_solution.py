import pytest

from y2025.src.day_01_solution import unlock

@pytest.fixture
def sample_input():
    return [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]


def test_unlock_with_sample_input(sample_input):
    result1, result2 = unlock(sample_input)
    assert result1 == 3
    assert result2 == 6