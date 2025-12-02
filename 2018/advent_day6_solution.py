import numpy as np
from collections import Counter
from itertools import product
from scipy.spatial.distance import cdist


def find_largest_space():
    with open("advent-input-day6", 'r') as f:
        coords = [tuple(map(int, line.split(','))) for line in f]
    
    # define dimensions of search grid
    left, top = np.amin(coords, axis=0)
    right, bottom = np.amax(coords, axis=0)
    
    grid = list(product(range(left, right + 1), range(top, bottom + 1)))
    
    # Matrix of distance from each grid point to each known coordinate
    dist_matrix = cdist(grid, coords, 'cityblock').astype(int)

    # Count the number of points that are closest to a known point.
    coord_area = Counter()
    for point_distances in dist_matrix:
        idx_min_dist = point_distances.argmin()
        if np.sum(point_distances == point_distances[idx_min_dist]) == 1:
            coord_area.update([idx_min_dist])

    # First four results are probably the corners (infinite), the fifth result is probably valid.
    biggest_area = coord_area.most_common(5)[-1][1]

    # Find the nuber of points where the sum all paths to a location is less than 10000
    most_central = np.sum(np.sum(dist_matrix, axis = 1) < 10000)
    
    return biggest_area, most_central

