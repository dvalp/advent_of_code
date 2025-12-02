import re
from typing import Iterable

import networkx as nx

BAG_COLOR = re.compile(r"^(?P<bag>\w+\s\w+)")
BAGS_CONTAINED = re.compile(r"(?P<contains>no other bags|(?:\d\s\w+\s+\w+))")


def build_graph(rules: Iterable[str]):
    G = nx.DiGraph()
    for rule in rules:
        G.add_weighted_edges_from(get_edges_from_bag(rule))
    return G


def get_edges_from_bag(line: str) -> tuple[str, str]:
    color = BAG_COLOR.match(line).group()
    for description in BAGS_CONTAINED.findall(line):
        if not description == "no other bags":
            count = int(description[0])
            bag = description[2:]
            yield color, bag, count


def count_all_children(graph: nx.DiGraph, node_name: str) -> int:
    if kids := graph.adj[node_name]:
        result = 1 + sum(node_data["weight"] * count_all_children(graph, child) for child, node_data in kids.items())
        return result
    return 1


if __name__ == '__main__':
    with open("../data/input_day07.txt") as f:
        bag_graph = build_graph(line.strip() for line in f)
    print(len(nx.ancestors(bag_graph, "shiny gold")))

    test_rules = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
    sample_graph = build_graph(line.strip() for line in test_rules.split("\n"))
    print(count_all_children(sample_graph, "shiny gold") - 1)
    print(count_all_children(bag_graph, "shiny gold") - 1)
