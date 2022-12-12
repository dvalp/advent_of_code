from pathlib import Path

import networkx as nx


def neighbor_in_range(current, neighbor):
    if current == "S":
        current = "a"
    elif current == "E":
        current = "z"
    if neighbor == "S":
        neighbor = "a"
    elif neighbor == "E":
        neighbor = "z"
    return ord(neighbor) - ord(current) <= 1


def transform_map(data: list[str]):
    height_map = [list(row) for row in data]
    inner_size = len(height_map[0])
    outer_size = len(height_map)
    coords = ((outer, inner) for outer in range(outer_size) for inner in range(inner_size))

    for outer, inner in coords:
        current = (outer, inner)
        current_value = height_map[outer][inner]

        valid_destinations = []
        neighbors = {(outer - 1, inner), (outer + 1, inner), (outer, inner - 1), (outer, inner + 1)}
        for point in neighbors:
            n_outer, n_inner = point
            if (0 <= n_outer < outer_size) and (0 <= n_inner < inner_size) \
                    and neighbor_in_range(current_value, height_map[n_outer][n_inner]):
                valid_destinations.append((n_outer, n_inner))

        yield current, current_value, valid_destinations


def process_map(elf_map):
    G = nx.DiGraph()
    for node, value, edges in transform_map(elf_map):
        G.add_node(node, value=value)
        G.add_edges_from((node, edge) for edge in edges)
    start_node = next(node for node, value in G.nodes.data("value") if value == "S")
    end_node = next(node for node, value in G.nodes.data("value") if value == "E")
    G.nodes[start_node]["value"] = "a"
    G.nodes[end_node]["value"] = "z"
    return G, start_node, end_node


def get_shortest_path_from_start(elf_map):
    G, start_node, end_node = process_map(elf_map=elf_map)
    return nx.shortest_path_length(G, start_node, end_node)


def get_any_shortest_path(elf_map):
    G, start_node, end_node = process_map(elf_map=elf_map)
    lowest_points = (node for node, value in G.nodes.data("value") if value == "a")
    shortest = -1
    for node in lowest_points:
        p_length = shortest
        try:
            p_length = nx.shortest_path_length(G, node, end_node)
        except nx.exception.NetworkXNoPath:
            pass

        if p_length < shortest or shortest < 0:
            shortest = p_length
    return shortest


if __name__ == '__main__':
    file_data = Path("../data/input_day_12.txt").read_text().strip().splitlines()
    print(get_shortest_path_from_start(file_data))
    print(get_any_shortest_path(file_data))
