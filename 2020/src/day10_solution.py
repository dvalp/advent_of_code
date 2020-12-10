from collections import Counter

import networkx as nx

RAW1 = """16
10
15
5
1
11
7
19
6
12
4
"""

RAW2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


def build_digraph(ratings: set[int]) -> nx.DiGraph:
    jolt_pairs = {(first_rating, converted)
                  for first_rating in ratings
                  for converted in {first_rating + 1, first_rating + 2, first_rating + 3}
                  if converted in ratings}
    G = nx.DiGraph()
    G.add_edges_from(jolt_pairs)
    return G


def calculate_joltage(ratings: set[int]) -> int:
    """This is what happens when you don't read instructions"""
    graph = build_digraph(ratings)
    return 3 + max(nx.descendants(graph, 0))


def calculate_jolt_distribution(ratings: set[int]) -> int:
    next_adaptor = list(ratings | {max(ratings) + 3})[1:]
    joltage_differences = zip(ratings, next_adaptor)
    j_dist = Counter((b - a) for a, b in joltage_differences)
    return j_dist[1] * j_dist[3]


def count_number_of_paths(ratings: set[int]) -> int:
    graph = build_digraph(ratings)
    path_counts = {}
    for adaptor in ratings:
        if adaptor == 0:
            path_counts[0] = 1
        elif adaptor in {1, 2}:
            path_counts[adaptor] = graph.in_degree[adaptor]
        else:
            n_paths = sum(path_counts.get(parent, 0) for parent in graph.predecessors(adaptor))
            path_counts[adaptor] = n_paths

    return path_counts[max(graph.nodes)]


if __name__ == '__main__':
    sample_input1 = {0} | {int(val) for val in RAW1.split()}
    sample_input2 = {0} | {int(val) for val in RAW2.split()}
    with open("../data/input_day10.txt", "r") as f:
        ratings_input = {0} | {int(line.strip()) for line in f}
    print(calculate_joltage(sample_input1))
    print(calculate_jolt_distribution(sample_input1))
    print(calculate_jolt_distribution(sample_input2))
    print(calculate_jolt_distribution(ratings_input))
    print(count_number_of_paths(sample_input2))
    print(count_number_of_paths(ratings_input))
