SAMPLE_DATA = """199
200
208
210
200
207
240
269
260
263"""


def count_increased_depth():
    with open("../data/input_day01.txt", "r") as f:
        count = 0
        prev = int(next(f))
        for line in f:
            curr = int(line)
            if curr > prev:
                count += 1
            prev = curr
    return count


def count_sliding_depth():
    with open("../data/input_day01.txt", "r") as f:
        data = [int(value) for value in f]
    count = 0
    for idx in range(len(data) - 3):
        if sum(data[idx:idx + 3]) < sum(data[idx + 1:idx + 4]):
            count += 1
    return count


def calculate_with_gap(gap: int = 1):
    """With thanks to Joel Grus for the idea"""
    with open("../data/input_day01.txt", "r") as f:
        data = [int(value) for value in f]
    count = 0
    for idx in range(len(data) - gap):
        if data[idx] < data[idx + gap]:
            count += 1
    return count


if __name__ == '__main__':
    print(count_increased_depth())
    print(calculate_with_gap(1))
    print(count_sliding_depth())
    print(calculate_with_gap(3))
