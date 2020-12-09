from pathlib import Path

RAW = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def stream_validation(stream: list[int], start_position: int = 5):
    for position in range(start_position, len(stream)):
        window = stream[position - start_position: position]
        target = stream[position]
        if not find_sum(window, target):
            print(target)
            return find_weakness(stream, target)


def find_sum(window, target) -> bool:
    results = []
    for idx, value in enumerate(window):
        other = target - value
        if other >= 0 and other in window[idx + 1:]:
            return True
        results.append(False)
    return any(results)


def find_weakness(stream, target):
    for idx in range(len(stream)):
        position = idx + 1
        result = -1
        while result < target:
            position += 1
            result = sum(stream[idx:position])

            if result == target:
                lo = min(stream[idx:position])
                hi = max(stream[idx:position])
                return sum([lo, hi])


if __name__ == '__main__':
    sample_stream = [int(val) for val in RAW.split()]
    input_stream = [int(line.strip()) for line in Path("../data/input_day09.txt").read_text().split()]

    print(stream_validation(sample_stream))
    print(find_weakness(sample_stream, 127))

    print(stream_validation(input_stream, 25))
