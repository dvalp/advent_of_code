import pytest
from src.day_08_solution import estimate_tree_cover


@pytest.fixture
def tree_map():
    return """30373
25512
65332
33549
35390""".splitlines()


def test_estimate_tree_cover(tree_map):
    assert estimate_tree_cover(tree_map) == (21, 8)
