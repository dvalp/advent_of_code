import pytest
from src.day_02_solution import first_game, second_game


@pytest.fixture
def data():
    return """A Y
B X
C Z""".split("\n")


def test_first_game(data):
    assert first_game(data) == 15


def test_second_game(data):
    assert second_game(data) == 12
