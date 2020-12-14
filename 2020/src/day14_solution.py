import re
from dataclasses import dataclass, field
from pathlib import Path

MEM_VALUE = re.compile(r"mem\[(?P<address>\d+)] = (?P<value>\d+)")


@dataclass
class DockingCode:
    mask: dict = field(default_factory=dict)
    codes: dict = field(default_factory=dict)

    @property
    def sum_values(self):
        return sum(self.codes.values())

    def modify_docking_values(self, program: list[str]) -> None:
        for line in program:
            if line.startswith("mask = "):
                self.mask = dict(
                    (idx, value) for idx, value in enumerate(line.removeprefix("mask = ").strip()) if value.isnumeric()
                )
            else:
                address, in_value = re.match(MEM_VALUE, line).group("address", "value")
                bin_value = dict(enumerate(format(int(in_value), '036b')))
                self.codes[address] = int(''.join((bin_value | self.mask).values()), 2)


if __name__ == '__main__':
    short_prog = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split("\n")
    docking_codes = Path("../data/input_day14.txt").read_text().strip().split("\n")

    sample_code = DockingCode()
    sample_code.modify_docking_values(short_prog)
    print(sample_code.codes)

    docking_program = DockingCode()
    docking_program.modify_docking_values(docking_codes)
    print(docking_program.sum_values)
