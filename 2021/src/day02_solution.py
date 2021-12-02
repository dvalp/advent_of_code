TEST_DIRECTIONS = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def get_directions():
    with open("../data/input_day02.txt", "r") as f:
        for line in f:
            direction, moves = line.split()
            yield direction, int(moves)


def navigation_first(commands: list[tuple[str, int]]):
    depth = 0
    distance = 0
    for command in commands:
        match command:
            case ("forward", moves):
                distance += moves
            case ("down", moves):
                depth += moves
            case ("up", moves):
                depth -= moves
    return depth * distance


def navigation_second(commands: list[tuple[str, int]]):
    aim = 0
    depth = 0
    distance = 0
    for command in commands:
        match command:
            case ("forward", moves):
                distance += moves
                depth += aim * moves
            case ("down", moves):
                aim += moves
            case ("up", moves):
                aim -= moves
    return depth * distance


if __name__ == '__main__':
    sample_commands = [(line.split()[0], int(line.split()[1])) for line in TEST_DIRECTIONS]
