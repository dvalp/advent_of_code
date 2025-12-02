import pytest
from y2023.src.day_03_solution import get_parts_total


@pytest.fixture
def schematic():
    return """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".strip().splitlines()


def test_get_parts_total(schematic):
    total, ratios = get_parts_total(schematic)
    assert total == 4361
    assert ratios == 467835
