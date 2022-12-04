from pathlib import Path


def find_overlap(data: list[str]) -> tuple[int, int]:
    contained_count = 0
    overlap_count = 0
    for team in data:
        areas = [tuple(int(val) for val in area.split("-")) for area in team.split(",")]
        sections = [set(range(area[0], area[1] + 1)) for area in areas]
        if (sections[0] < sections[1]) or (sections[0] >= sections[1]):
            contained_count += 1
        if sections[0] & sections[1]:
            overlap_count += 1
    return contained_count, overlap_count


if __name__ == '__main__':
    file_data = Path("../data/input_day_04.txt").read_text().strip().splitlines()
    print(find_overlap(file_data))
