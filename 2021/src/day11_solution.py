from pathlib import Path

import networkx as nx

SAMPLE_DATA = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split()


def convert_matrix_to_graph(input_data: list[str]) -> nx.Graph:
    octo_grid = nx.Graph()
    for row, line in enumerate(input_data):
        for column, level in enumerate(line):
            octo_grid.add_node((row, column), level=int(level))

            neighbors = {(row, column - 1), (row - 1, column - 1), (row - 1, column), (row - 1, column + 1)}
            for neighbor in neighbors:
                if octo_grid.has_node(neighbor):
                    octo_grid.add_edge((row, column), neighbor)
    return octo_grid


def count_flashes(input_data: list[str], iterations: int = 100):
    octo_graph = convert_matrix_to_graph(input_data)
    flashes = 0
    for step in range(iterations):
        for octopus in octo_graph:
            octo_graph.nodes[octopus]["level"] += 1

        flashed_octos = set()
        unflashed_octos = [octo for octo, level in octo_graph.nodes.data("level") if level > 9]
        while unflashed_octos:
            for octo in unflashed_octos:
                for coord in octo_graph.adj[octo]:
                    octo_graph.nodes[coord]["level"] += 1
                flashed_octos.add(octo)
            unflashed_octos = [octo for octo, level in octo_graph.nodes.data("level")
                               if level > 9 and octo not in flashed_octos]

        new_flashes = len(flashed_octos)
        flashes += new_flashes
        if new_flashes == 100:
            print(step + 1, new_flashes)

        for octopus, level in octo_graph.nodes.data("level"):
            if level > 9:
                octo_graph.nodes[octopus]["level"] = 0

    return flashes


if __name__ == '__main__':
    file_data = Path("../data/input_day11.txt").read_text().strip().split("\n")
    # print(count_flashes(SAMPLE_DATA))
    # print(count_flashes(file_data))
    print("Sample\n")
    print(count_flashes(SAMPLE_DATA, 200))
    print("\nReal\n")
    print(count_flashes(file_data, 300))
