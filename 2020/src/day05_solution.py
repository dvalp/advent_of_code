from collections import namedtuple, deque
from pathlib import Path

SampleID = namedtuple("SampleID", "code row column id")
SAMPLES = [
    SampleID("FBFBBFFRLR", 44, 5, 357),
    SampleID("BFFFBBFRRR", 70, 7, 567),
    SampleID("FFFBBBFRRR", 14, 7, 119),
    SampleID("BBFFBBFRLL", 102, 4, 820),

]

LO_CODES = {"F", "L"}
HI_CODES = {"B", "R"}


def seat_finder(boarding_pass: str) -> int:
    row_range = (0, 127)
    column_range = (0, 7)
    row_code = deque(boarding_pass[:7])
    column_code = deque(boarding_pass[7:])
    row = _binary_search(row_code, row_range)
    column = _binary_search(column_code, column_range)
    seat_id = row * 8 + column
    return seat_id


def _binary_search(code: deque, search_space: tuple) -> int:
    value = code.popleft()
    lo, hi = search_space

    if value not in LO_CODES | HI_CODES:
        raise ValueError("Invalid code was received")

    if not code:
        if not hi - lo == 1:
            raise ValueError("Search space failed to reduce to size 2")
        if value in LO_CODES:
            return lo
        else:
            return hi
    else:
        diff = (hi - lo) // 2
        if value in LO_CODES:
            hi = lo + diff
        elif value in HI_CODES:
            lo = hi - diff
        return _binary_search(code, (lo, hi))


def find_highest_seat_id(codes: set[str]) -> int:
    return max(seat_finder(code) for code in codes)


def find_missing_seat(codes: set[str]) -> int:
    seat_ids = {seat_finder(code) for code in codes}
    possible_ids = {*range(min(seat_ids), max(seat_ids) + 1)}
    return (possible_ids - seat_ids).pop()


def simpler_seat_id():
    """Including this as a reminder that a different perspective can help"""
    fpath = Path("../data/input_day05.txt")
    tl = str.maketrans('FBLR', '0101')
    ids = {int(code.translate(tl), 2) for code in Path.read_text(fpath).split()}
    return max(ids), max({*range(max(ids))} - ids)


if __name__ == '__main__':
    print(seat_finder(SAMPLES[0].code))
    seat_codes = {sample.code for sample in SAMPLES}
    print(find_highest_seat_id(seat_codes))

    with open("../data/input_day05.txt")as f:
        all_codes = {line.strip() for line in f}
    print(find_highest_seat_id(all_codes))
    print(find_missing_seat(all_codes))
    print(simpler_seat_id())
