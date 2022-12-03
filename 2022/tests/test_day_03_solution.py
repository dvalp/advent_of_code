import pytest
from src.day_03_solution import inspect_packing, find_badges


@pytest.fixture
def data():
    return """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()


def test_inspect_packing(data):
    assert inspect_packing(data) == 157


def test_find_badges(data):
    assert find_badges(data) == 70
