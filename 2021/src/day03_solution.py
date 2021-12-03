from collections import Counter, defaultdict
from typing import Iterable

import numpy as np

SAMPLE_DATA = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".strip().split()


def get_data():
    with open("../data/input_day03.txt", "r") as f:
        for line in f:
            yield line.strip()


def part1(data: Iterable):
    counts = defaultdict(Counter)
    gamma_bits = []
    epsilon_bits = []

    for line in data:
        for idx, bit in enumerate(line):
            counts[idx][bit] += 1

    for idx, bits in counts.items():
        gamma_bits.append(bits.most_common()[0][0])
        epsilon_bits.append(bits.most_common()[1][0])

    gamma = int("".join(gamma_bits), 2)
    epsilon = int("".join(epsilon_bits), 2)

    return gamma * epsilon


def part2(data: Iterable):
    idx = 0
    o2_matrix = co2_matrix = np.array([[int(digit) for digit in line] for line in data])
    calc_o2 = calc_co2 = True
    while calc_o2 or calc_co2:
        if calc_o2:
            o2_count = np.bincount(o2_matrix[:, idx])
            o2_digit = 1 if np.all(o2_count == o2_count[0]) else o2_count.argmax()
            o2_matrix = o2_matrix[o2_matrix[:, idx] == o2_digit]
            calc_o2 = len(o2_matrix) > 1

        if calc_co2:
            co2_count = np.bincount(co2_matrix[:, idx])
            co2_digit = 0 if np.all(co2_count == co2_count[0]) else co2_count.argmin()
            co2_matrix = co2_matrix[co2_matrix[:, idx] == co2_digit]
            calc_co2 = len(co2_matrix) > 1

        idx += 1

    o2_rating = int("".join(str(value) for value in o2_matrix[0]), 2)
    co2_rating = int("".join(str(value) for value in co2_matrix[0]), 2)

    return o2_rating * co2_rating


if __name__ == '__main__':
    print(part1(get_data()))
    print(part2(get_data()))
