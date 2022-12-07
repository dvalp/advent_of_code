from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


@dataclass
class Directory:
    name: str
    parent: Directory | None
    subdirs: dict[str, Directory] = field(default_factory=dict)
    files: dict[str, int] = field(default_factory=dict)

    def create_subdir(self, name: str):
        self.subdirs[name] = Directory(name, self)

    def create_file(self, name: str, desc: str):
        self.files[name] = int(desc)

    @property
    def dir_size(self) -> int:
        return sum(self.files.values()) + sum(subdir.dir_size for subdir in self.subdirs.values())

    def get_all_directory_sizes(self) -> Iterable[int]:
        for subdir in self.subdirs.values():
            yield from subdir.get_all_directory_sizes()
        yield self.dir_size

    def sum_small_dirs(self, threshold: int = 100_000) -> int:
        return sum(dir_size for dir_size in self.get_all_directory_sizes() if dir_size <= threshold)

    def min_size_to_clear(self, required_space: int = 30_000_000, disk_size: int = 70_000_000) -> int:
        unused_space = disk_size - self.dir_size
        space_needed = required_space - unused_space
        return min(dir_size for dir_size in self.get_all_directory_sizes() if dir_size >= space_needed)

    @staticmethod
    def parse_fs_data(fs_data: list[str]) -> Directory:
        root = Directory("/", parent=None)
        current = root
        for line in fs_data:
            match line.split():
                case "$", "cd", "/":
                    current = root
                case "$", "cd", "..":
                    current = current.parent
                case "$", "cd", name:
                    current = current.subdirs[name]
                case desc, name if desc.isdecimal():
                    current.create_file(name=name, desc=desc)
                case desc, name if desc == "dir":
                    current.create_subdir(name)
                case _:
                    pass

        return root


if __name__ == '__main__':
    file_data = Path("../data/input_day_07.txt").read_text().strip().splitlines()
    fs = Directory.parse_fs_data(file_data)
    print(fs.sum_small_dirs())
    print(fs.min_size_to_clear())
