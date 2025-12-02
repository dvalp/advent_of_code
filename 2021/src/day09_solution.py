from pathlib import Path

import networkx as nx
import numpy as np

SAMPLE_DATA = """2199943210
3987894921
9856789892
8767896789
9899965678""".split()


def risk_sum(input_data):
    cave_map = np.array([[int(value) for value in line] for line in input_data])
    padded_map = np.pad(cave_map, 1, 'constant', constant_values=10)

    p1_result = 0
    max_row, max_col = cave_map.shape
    G = nx.Graph()

    for row in range(1, max_row + 1):
        for column in range(1, max_col + 1):
            location = row, column
            current_value = padded_map[location]
            row_idx = [row - 1, row, row + 1, row]
            column_idx = [column, column + 1, column, column - 1]
            neighbors = padded_map[row_idx, column_idx]
            if (neighbors > current_value).all():
                p1_result += current_value + 1
            if current_value < 9:
                G.add_node(location)
                for neighbor_coord in zip(row_idx, column_idx):
                    if padded_map[neighbor_coord] < 9:
                        G.add_edge(location, neighbor_coord)

    p2_result = np.prod([len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)][:3])

    return p1_result, p2_result


if __name__ == '__main__':
    file_data = Path("../data/input_day09.txt").read_text().strip().split("\n")
    print(risk_sum(SAMPLE_DATA))
    print(risk_sum(file_data))
