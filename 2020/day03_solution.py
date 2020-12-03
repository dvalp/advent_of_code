def tree_count():
    horiz = 0

    with open("data/input_day03.txt", "r") as f:
        next(f)
        for line in f:
            horiz += 3
            yield line[horiz % 31] == '#'


if __name__ == '__main__':
    sum(tree_count())
