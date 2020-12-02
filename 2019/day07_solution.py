from itertools import permutations
from typing import List, Optional, Iterable


def int_comp(inputs: list):
    with open("input_day07", "r") as f:
        memory = [int(term) for term in f.read().strip().split(",")]

    idx = 0
    while memory[idx] != 99:
        code_string = f"{memory[idx]:0>5}"
        op_mode3 = int(code_string[0])
        op_mode2 = int(code_string[1])
        op_mode1 = int(code_string[2])
        op = int(code_string[-2:])

        if op in [1, 2, 5, 6, 7, 8]:
            if op_mode1:    # immediate mode
                first = memory[idx + 1]
            else:           # position mode
                first = memory[memory[idx + 1]]

            if op_mode2:
                second = memory[idx + 2]
            else:
                second = memory[memory[idx + 2]]

        if op == 1:
            dest = memory[idx + 3]
            memory[dest] = sum((first, second))
            idx += 4
        elif op == 2:
            dest = memory[idx + 3]
            memory[dest] = first * second
            idx += 4
        elif op == 3:
            dest = memory[idx + 1]
            # memory[dest] = int(input("Enter system code: "))
            memory[dest] = inputs.pop(0)
            idx += 2
        elif op == 4:
            if op_mode1:
                value = memory[idx + 1]
            else:
                value = memory[memory[idx + 1]]
            yield value
            idx += 2
        elif op == 5:
            if first != 0:
                idx = second
            else:
                idx += 3
        elif op == 6:
            if first == 0:
                idx = second
            else:
                idx += 3
        elif op == 7:
            dest = memory[idx + 3]
            if first < second:
                memory[dest] = 1
            else:
                memory[dest] = 0
            idx += 4
        elif op == 8:
            dest = memory[idx + 3]
            if first == second:
                memory[dest] = 1
            else:
                memory[dest] = 0
            idx += 4


def run_amplifier():
    perms = permutations([0, 1, 2, 3, 4])
    max_result = 0
    for instance in perms:
        result = 0
        for phase in instance:
            result = int_comp([result, phase])
        if result > max_result:
            max_result = result

    print(max_result)


def run_amplifier_indefinite():
    m = (0, tuple())
    for phases in permutations(range(5, 10)):
        signal = 0
        pipes = [[phase] for phase in phases]
        computers = [int_comp(phase) for phase in pipes]
        try:
            while True:
                for i, phase in enumerate(phases):
                    pipes[i].append(signal)
                    signal = next(computers[i])
        except StopIteration:
            pass
        m = max(m, (signal, phases))

    print(m)


if __name__ == '__main__':
    run_amplifier_indefinite()
