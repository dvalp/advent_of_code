import networkx as nx


def count_orbits():
    with open("input_day06", "r") as f:
        edges = [edge.strip().split(")") for edge in f]

    G = nx.Graph()
    G.add_edges_from(edges)
    paths = nx.shortest_path(G, "COM")
    return {"orbits":        sum((len(p) - 1) for p in paths.values()),
            "steps_YOU_SAN": len(nx.shortest_path(G, "YOU", "SAN")) - 3}
