from collections import defaultdict, namedtuple
from pathlib import Path

ResultValues = namedtuple("ResultValues", "points counts")


def calculate_points(cards):
    points = 0
    card_counts = defaultdict(int)
    for idx, card in enumerate(cards, start=1):
        card_counts[idx] += 1

        groups = card.split(":")[1].split("|")
        winners = set(groups[0].split())
        numbers = groups[1].split()
        wins = sum(1 for value in numbers if value in winners)

        if wins > 0:
            points += 2 ** (wins - 1)

        for card_number in range(idx + 1, idx + wins + 1):
            card_counts[card_number] += card_counts[idx]

    return ResultValues(points, sum(card_counts.values()))


if __name__ == '__main__':
    file_data = Path("y2023/data/input_day04.txt").read_text().strip().splitlines()
    print(calculate_points(file_data))
