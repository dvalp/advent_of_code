import pytest
from src.day_01_solution import get_calorie_values, simpler_calorie_counts


@pytest.fixture
def calories():
    return """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".strip()


@pytest.mark.parametrize("count,expected", [(1, 24000), (3, 45000)])
def test_get_calorie_values(calories, count, expected):
    assert get_calorie_values(data=calories.split("\n"), count=count) == expected


@pytest.mark.parametrize("count,expected", [(1, 24000), (3, 45000)])
def test_simpler_calorie_counts(calories, count, expected):
    assert simpler_calorie_counts(data=calories, count=count) == expected
