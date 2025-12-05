import pytest

from y2025.src.day_04_solution import count_roles, char_translation


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
