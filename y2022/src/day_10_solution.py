from dataclasses import dataclass, field
from pathlib import Path

import numpy as np


@dataclass
class VideoMonitor:
    x_register: int = 1
    cycle: int = 0
    interesting_signals: list[int] = field(default_factory=list)
    active_pixels: list[str] = field(default_factory=list)

    def run_cycles(self, count: int):
        for _ in range(count):
            current_position = self.cycle % 40
            if (self.x_register - 1) <= current_position <= (self.x_register + 1):
                self.active_pixels.append("#")
            else:
                self.active_pixels.append(".")

            self.cycle += 1

            if (self.cycle >= 20) and ((self.cycle - 20) % 40 == 0):
                self.interesting_signals.append(self.x_register * self.cycle)

    def parse_signal(self, instructions: list[str]):
        for instruction in instructions:
            match instruction.split():
                case ["noop"]:
                    self.run_cycles(1)
                case ["addx", value]:
                    self.run_cycles(2)
                    self.x_register += int(value)

    @property
    def sum_interesting_signals(self) -> int:
        return sum(self.interesting_signals)

    @property
    def crt_image(self) -> str:
        return "\n".join("".join(line) for line in np.array(self.active_pixels).reshape(6, -1))


if __name__ == '__main__':
    file_data = Path("../data/input_day_10.txt").read_text().strip().splitlines()
    monitor = VideoMonitor()
    monitor.parse_signal(file_data)
    print(monitor.sum_interesting_signals)
    print(monitor.crt_image)
