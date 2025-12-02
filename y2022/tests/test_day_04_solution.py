import pytest
from src.day_04_solution import find_overlap


@pytest.fixture
def data():
    return """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()


def test_find_overlap(data):
    assert find_overlap(data) == 2
