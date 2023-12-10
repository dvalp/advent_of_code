import re
from collections import defaultdict, namedtuple
from pathlib import Path


gear_results = namedtuple("gear_results", ["total", "ratio"])


def get_parts_total(schematic):
    number_pattern = re.compile(r"\d+")
    gear_pattern = re.compile(r"\*")
    gear_groups = defaultdict(list)
    total = 0
    ratio_total = 0

    for line_idx, line in enumerate(schematic):
        for match in number_pattern.finditer(line):
            neighbors = set()
            start = match.start() - 1 if match.start() > 0 else 0
            end = match.end() + 1 if match.end() < len(line) else match.end()

            if match.start() > 0:
                left = line[match.start() - 1]
                neighbors.add(left)
                if left == "*":
                    gear_groups[(match.start() - 1, line_idx)].append(int(match.group(0)))
            if match.end() < len(line):
                right = line[match.end()]
                neighbors.add(right)
                if right == "*":
                    gear_groups[(match.end(), line_idx)].append(int(match.group(0)))
            if line_idx > 0:
                upper = schematic[line_idx - 1][start:end]
                neighbors.update(upper)
                for gear in gear_pattern.finditer(upper):
                    gear_groups[(gear.start() + start, line_idx - 1)].append(int(match.group(0)))
            if line_idx < len(schematic) - 1:
                lower = schematic[line_idx + 1][start:end]
                neighbors.update(lower)
                for gear in gear_pattern.finditer(lower):
                    gear_groups[(gear.start() + start, line_idx + 1)].append(int(match.group(0)))

            if neighbors - set("0123456789."):
                total += int(match.group(0))

    for parts in gear_groups.values():
        if len(parts) == 2:
            ratio_total += parts[0] * parts[1]

    return gear_results(total, ratio_total)


if __name__ == '__main__':
    file_data = Path("y2023/data/input_day03.txt").read_text().strip().splitlines()
    print(get_parts_total(file_data))
