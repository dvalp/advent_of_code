import re
from dataclasses import dataclass, field
from itertools import product
from pathlib import Path

MEM_VALUE = re.compile(r"mem\[(?P<address>\d+)] = (?P<value>\d+)")


@dataclass
class DockingCode:
    mask: dict[int, str] = field(default_factory=dict)
    codes: dict[str, int] = field(default_factory=dict)
    float_masks: list[dict[int, str]] = field(default_factory=list)

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

    def modify_memory_ids(self, program: list[str]) -> None:
        for line in program:
            if line.startswith("mask = "):
                mask = line.removeprefix("mask = ").strip()
                self.mask = dict((idx, value) for idx, value in enumerate(mask) if value == "1")
                float_ids = [idx for idx, mem_id in enumerate(mask) if mem_id == "X"]
                self.float_masks = [dict(zip(float_ids, values)) for values in product({"1", "0"}, repeat=len(float_ids))]
            else:
                address, in_value = re.match(MEM_VALUE, line).group("address", "value")
                bin_address = dict(enumerate(format(int(address), '036b')))
                for float_mask in self.float_masks:
                    modified_address = str(int("".join((bin_address | self.mask | float_mask).values()), 2))
                    self.codes[modified_address] = int(in_value)


if __name__ == '__main__':
    short_prog = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split("\n")
    docking_codes = Path("../data/input_day14.txt").read_text().strip().split("\n")

    sample_code = DockingCode()
    sample_code.modify_docking_values(short_prog)
    print(sample_code.codes)
    print(sample_code.sum_values)

    docking_program = DockingCode()
    docking_program.modify_docking_values(docking_codes)
    print(docking_program.sum_values)

    docking_program2 = DockingCode()
    docking_program2.modify_memory_ids(docking_codes)
    print(docking_program2.sum_values)
