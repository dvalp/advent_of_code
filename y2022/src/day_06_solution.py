from pathlib import Path


def find_start(data: str, length: int) -> int:
    start_process = -1
    for idx, character in enumerate(data, start=1):
        if idx >= length:
            if length == len(set(data[idx - length: idx])):
                start_process = idx
                break
    return start_process


if __name__ == '__main__':
    file_data = Path("../data/input_day_06.txt").read_text().strip()
    print(find_start(file_data, 4))
    print(find_start(file_data, 14))
