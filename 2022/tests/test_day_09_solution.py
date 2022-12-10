import pytest
from src.day_09_solution import track_path, track_path2


@pytest.fixture
def route_directions():
    return """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

@pytest.fixture
def route_directions2():
    return """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines()


def test_track_path(route_directions):
    assert track_path(route_directions) == 13

def test_track_path2(route_directions):
    assert track_path2(route_directions, 10) == 1

def test_track_path2_tail_moves(route_directions2):
    assert track_path2(route_directions2, 10) == 36
