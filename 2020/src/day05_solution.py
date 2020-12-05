from collections import namedtuple, deque

SampleID = namedtuple("SampleID", "code row column id")
SAMPLES = [
    SampleID("FBFBBFFRLR", 44, 5, 357),
    SampleID("BFFFBBFRRR", 70, 7, 567),
    SampleID("FFFBBBFRRR", 14, 7, 119),
    SampleID("BBFFBBFRLL", 102, 4, 820),

]

LO_CODES = {"F", "L"}
HI_CODES = {"B", "R"}


def seat_finder_01(boarding_pass: str) -> int:
    rows = (0, 127)
    columns = (0, 7)
    row_code = deque(boarding_pass[:7])
    column_code = deque(boarding_pass[7:])
    row = _binary_search(row_code, rows)
    column = _binary_search(column_code, columns)
    seat_id = row * 8 + column
    return seat_id


def _binary_search(code: deque, search_space: tuple) -> int:
    print(code)
    value = code.popleft()
    lo, hi = search_space

    if value not in LO_CODES | HI_CODES:
        raise ValueError("Invalid code was received")

    if not code:
        if not hi - lo == 1:
            raise ValueError("Search space failed to reduce to size 2")
        if value in {"F", "L"}:
            return lo
        else:
            return hi
    else:
        diff = hi - lo
        if value in LO_CODES:
            hi -= diff
        elif value in HI_CODES:
            lo += diff
        return _binary_search(code, (lo, hi))


def find_highest_seat_id():
    pass
