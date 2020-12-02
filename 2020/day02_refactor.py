from __future__ import annotations

import re
from typing import NamedTuple


class Password(NamedTuple):
    lo: int
    hi: int
    letter: str
    pwd: str

    def validate(self) -> bool:
        return int(self.lo) <= self.pwd.count(self.letter) <= int(self.hi)

    def validate2(self) -> bool:
        first = self.pwd[int(self.lo) - 1] == self.letter
        second = self.pwd[int(self.hi) - 1] == self.letter
        return first ^ second

    @staticmethod
    def parse_line(line: str) -> Password:
        pos1, pos2, letter, _, pwd = re.split("[-: ]", line)
        return Password(pos1, pos2, letter, pwd)


if __name__ == '__main__':
    with open("data/input_day02.txt", "r") as f:
        print(sum(Password.parse_line(line).validate2() for line in f))
