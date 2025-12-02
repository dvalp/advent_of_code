import pytest
from src.day_12_solution import get_shortest_path_from_start, get_any_shortest_path


@pytest.fixture
def height_map():
    return """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()


def test_get_shortest_path_from_start(height_map):
    assert get_shortest_path_from_start(height_map) == 31


def test_get_any_shortest_path(height_map):
    assert get_any_shortest_path(height_map) == 29
