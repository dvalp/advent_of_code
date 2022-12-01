import pytest
from src.day_01_solution import get_calorie_values


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
    
    10000""".strip().split("\n")


@pytest.mark.parametrize("count,expected", [(1, 24000), (3, 45000)])
def test_get_calorie_values(calories, count, expected):
    assert get_calorie_values(data=calories, count=count) == expected
