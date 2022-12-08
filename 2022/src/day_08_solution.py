import numpy as np
from pathlib import Path


def estimate_tree_cover(tree_map: list[str]) -> tuple[int, int]:
    trees = np.array([list(row) for row in tree_map]).astype(int)
    x_limit, y_limit = (val -1 for val in trees.shape)
    cover_map = np.ones_like(trees)
    cover_map[1:x_limit, 1:y_limit] = 0  # outer edge is visible (ie, =1)
    max_scenic = 0
    coords = ((x, y) for x in np.arange(1, x_limit) for y in np.arange(1, y_limit))
    for outer, inner in coords:
        sightlines = [
            trees[:outer, inner][::-1],
            trees[outer + 1:, inner],
            trees[outer, :inner][::-1],
            trees[outer, inner + 1:]
        ]
        if any(trees[outer, inner] > view.max() for view in sightlines):
            cover_map[outer, inner] = 1

        if (scenic_score := evaluate_views(sightlines, trees[outer, inner])) > max_scenic:
            max_scenic = scenic_score
    return cover_map.sum(), max_scenic


def evaluate_views(sightlines: list[np.array], height: int) -> np.array:
    view_scores = []
    for view in sightlines:
        if np.any(blocks := (view >= height)):
            view_scores.append(np.argmax(blocks) + 1)
        else:
            view_scores.append(len(view))
    return np.prod(view_scores)


if __name__ == '__main__':
    file_data = Path("../data/input_day_08.txt").read_text().strip().splitlines()
    print(estimate_tree_cover(file_data))
