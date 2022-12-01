from pathlib import Path

import networkx as nx

SAMPLE_A = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split()

SAMPLE_B = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".split()


def count_paths(input_data: list[str]) -> int:
    cave_map = nx.Graph()
    cave_map.add_edges_from(line.split("-") for line in input_data)


if __name__ == '__main__':
    file_data = Path("../data/input_day11.txt").read_text().strip().split("\n")
