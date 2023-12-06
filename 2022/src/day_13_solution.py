import ast
from enum import IntEnum, auto
from functools import cmp_to_key
from itertools import zip_longest
from pathlib import Path


class Results(IntEnum):
    ORDERED = -1
    UNORDERED = 1
    EQUAL = 0


def process_packets(packet_data: list[str]):
    success = []
    for idx, packet_pair in enumerate(packet_data, start=1):
        left, right = [ast.literal_eval(packet) for packet in packet_pair.splitlines()]
        if evaluate_packets(left, right) is not Results.UNORDERED:
            success.append(idx)
    return sum(success)


def evaluate_packets(left, right):
    for left_item, right_item in zip_longest(left, right):
        if isinstance(left_item, int) and isinstance(right_item, int):
            if left_item < right_item:
                return Results.ORDERED
            elif left_item > right_item:
                return Results.UNORDERED
        elif left_item == right_item:
            continue
        elif right_item != 0 and not right_item:
            return Results.UNORDERED
        elif not left_item:
            return Results.ORDERED
        else:
            left_item = [left_item] if isinstance(left_item, int) else left_item
            right_item = [right_item] if isinstance(right_item, int) else right_item
            if (result := evaluate_packets(left_item, right_item)) != Results.EQUAL:
                return result
    return Results.EQUAL


def get_decoder_key(packet_data):
    div1 = [[2]]
    div2 = [[6]]
    packets = [ast.literal_eval(packet) for packet_pair in packet_data for packet in packet_pair.splitlines()]
    packets.extend([div1, div2])

    packets = sorted(packets, key=cmp_to_key(evaluate_packets))
    return (packets.index(div1) + 1) * (packets.index(div2) + 1)


if __name__ == '__main__':
    file_data = Path("../data/input_day_13.txt").read_text().strip().split("\n\n")
    print(process_packets(file_data))
    print(get_decoder_key(file_data))
