from collections import defaultdict

test_numbers = [
    ([0, 3, 6], 436),
    ([1, 3, 2], 1),
    ([2, 1, 3], 10),
    ([1, 2, 3], 27),
    ([2, 3, 1], 78),
    ([3, 2, 1], 438),
    ([3, 1, 2], 1836)
]
test_numbers_p2 = [
    ([0, 3, 6], 175594),
    ([1, 3, 2], 2578),
    ([2, 1, 3], 3544142),
    ([1, 2, 3], 261214),
    ([2, 3, 1], 6895259),
    ([3, 2, 1], 18),
    ([3, 1, 2], 362),
]
puzzle_input = [13, 0, 10, 12, 1, 5, 8]


def memory_game(numbers: list[int], final_value: int = 2020) -> int:
    memory = defaultdict(list)
    previous_number = numbers[-1]
    for idx, value in enumerate(numbers):
        memory[value].append(idx)

    for idx in range(len(numbers), final_value):
        if len(memory[previous_number]) == 1:
            new_number = 0
            memory[new_number].append(idx)
        elif len(memory[previous_number]) > 1:
            new_number = memory[previous_number][-1] - memory[previous_number][-2]
            memory[new_number].append(idx)
        else:
            raise ValueError("Oops, something went wrong and that number hasn't been said")
        previous_number = new_number
    print(previous_number)
    return previous_number


if __name__ == '__main__':
    # for test_input, test_result in test_numbers:
    #     print(f"Testing: {test_result}")
    #     assert memory_game(test_input) == test_result

    # for test_input, test_result in test_numbers_p2:
    #     print(f"Testing p2: {test_result}")
    #     assert memory_game(test_input, final_value=30000000) == test_result

    print("Challenge result p2:", memory_game(puzzle_input, final_value=30000000))
