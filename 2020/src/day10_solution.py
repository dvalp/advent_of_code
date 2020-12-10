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


def calculate_joltage(ratings: set[int]) -> int:
    """This is what happens when you don't read instructions"""
    root_node = {(0, value) for value in {1, 2, 3} if value in ratings}
    jolt_pairs = {(first_rating, converted)
                  for first_rating in ratings
                  for converted in {first_rating + 1, first_rating + 2, first_rating + 3}
                  if converted in ratings}
    G = nx.DiGraph()
    G.add_edges_from(root_node | jolt_pairs)
    return 3 + max(nx.descendants(G, 0))


def calculate_jolt_distribution(ratings: set[int]) -> int:
    joltage_differences = zip(ratings | {0}, ratings | {max(ratings) + 3})
    j_dist = Counter((b - a) for a, b in joltage_differences)
    return j_dist[1] * j_dist[3]


if __name__ == '__main__':
    sample_input1 = {int(val) for val in RAW1.split()}
    sample_input2 = {int(val) for val in RAW2.split()}
    with open("../data/input_day10.txt", "r") as f:
        ratings_input = {int(line.strip()) for line in f}
    print(calculate_joltage(sample_input1))
    print(calculate_jolt_distribution(sample_input1))
    print(calculate_jolt_distribution(sample_input2))
    print(calculate_jolt_distribution(ratings_input))
