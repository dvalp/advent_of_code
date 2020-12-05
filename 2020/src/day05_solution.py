from collections import namedtuple

SampleID = namedtuple("SampleID", "code row column id")
SAMPLES = [
    SampleID("FBFBBFFRLR", 44, 5, 357),
    SampleID("BFFFBBFRRR", 70, 7, 567),
    SampleID("FFFBBBFRRR", 14, 7, 119),
    SampleID("BBFFBBFRLL", 102, 4, 820),

]


def seat_finder_01(boarding_pass: str):
    rows = 128
    seats = 8
    row_code = boarding_pass[:7]
    column_code = boarding_pass[7:]

    seat_id = row * 8 + column


def find_highest_seat_id():
    pass
