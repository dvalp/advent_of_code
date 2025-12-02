import pytest
from src.day_07_solution import Directory


@pytest.fixture
def file_system():
    fs_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()
    return Directory.parse_fs_data(fs_data)


def test_parse_fs_data(file_system):
    assert file_system.sum_small_dirs() == 95437


def test_min_size_to_clear(file_system):
    assert file_system.min_size_to_clear() == 24933642
