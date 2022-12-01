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


def test_get_calorie_values(calories):
    assert get_calorie_values(calories) == 24000
    assert get_calorie_values(calories, 3) == 45000

