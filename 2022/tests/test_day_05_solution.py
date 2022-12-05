from collections import deque

import pytest
from src.day_05_solution import restack_crates, restack_crates_upgrade


@pytest.fixture
def moves():
    return """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()


@pytest.fixture
def arrangement():
    return {
        1: deque(["Z", "N"]),
        2: deque(["M", "C", "D"]),
        3: deque(["P"])
    }


def test_restack_crates(moves, arrangement):
    assert restack_crates(moves, arrangement) == "CMZ"


def test_restack_crates_upgrade(moves, arrangement):
    assert restack_crates_upgrade(moves, arrangement) == "MCD"
