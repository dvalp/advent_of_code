def int_comp(inputs: list):
    with open("input_day09", "r") as f:
        memory = [int(term) for term in f.read().strip().split(",")]
    # memory = [104,1125899906842624,99]
    memory.extend([0] * 1000)
    idx = 0
    relative_base = 0
    while memory[idx] != 99:
        code_string = f"{memory[idx]:0>5}"
        op_mode3 = int(code_string[0])
        op_mode2 = int(code_string[1])
        op_mode1 = int(code_string[2])
        op = int(code_string[-2:])

        if op_mode1 == 0:           # position mode
            first = memory[memory[idx + 1]]
        elif op_mode1 == 1:         # immediate mode
            first = memory[idx + 1]
        elif op_mode1 == 2:         # relative mode
            first = memory[memory[idx + 1] + relative_base]

        if op in [1, 2, 5, 6, 7, 8]:
            if op_mode2 == 0:
                second = memory[memory[idx + 2]]
            elif op_mode2 == 1:
                second = memory[idx + 2]
            elif op_mode2 == 2:
                second = memory[memory[idx + 2] + relative_base]

        if op in [1, 2, 7, 8]:
            if op_mode3 == 0:
                dest = memory[idx + 3]
            elif op_mode3 == 2:
                dest = memory[idx + 3] + relative_base

        if op == 1:
            memory[dest] = sum((first, second))
            idx += 4
        elif op == 2:
            memory[dest] = first * second
            idx += 4
        elif op == 3:
            if op_mode1 == 0:
                dest = memory[idx + 1]
            if op_mode1 == 2:
                dest = memory[idx + 1] + relative_base
            # memory[dest] = int(input("Enter system code: "))
            memory[dest] = inputs.pop(0)
            idx += 2
        elif op == 4:
            value = first
            # print(value)
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
            if first < second:
                memory[dest] = 1
            else:
                memory[dest] = 0
            idx += 4
        elif op == 8:
            if first == second:
                memory[dest] = 1
            else:
                memory[dest] = 0
            idx += 4
        elif op == 9:
            relative_base += first
            idx += 2
        else:
            raise Exception(f"Invalid op code: {op}\n Op context: {code_string, idx, memory[idx:idx + 4]}")


if __name__ == '__main__':
    comp = int_comp([2])
    code = []
    for result in comp:
        print(result)
    print(code)
