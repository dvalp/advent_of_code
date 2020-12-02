

arr = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]


def process_data(memory):
    memory[1] = 12
    memory[2] = 2
    for start in range(0, len(memory), 4):
        entry = memory[start:start + 4]

        if entry[0] == 99:
            break
        elif entry[0] == 1:
            memory[entry[3]] = memory[entry[1]] + memory[entry[2]]
        elif entry[0] == 2:
            memory[entry[3]] = memory[entry[1]] * memory[entry[2]]
    return memory[0]


def process_data_pattern():
    for noun in range(100):
        for verb in range(100):
            memory = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]
            memory[1] = noun
            memory[2] = verb

            for start in range(0, len(memory), 4):
                entry = memory[start:start + 4]

                if entry[0] == 99:
                    break
                elif entry[0] == 1:
                    memory[entry[3]] = memory[entry[1]] + memory[entry[2]]
                elif entry[0] == 2:
                    memory[entry[3]] = memory[entry[1]] * memory[entry[2]]
            if memory[0] == 19690720:
                return 100 * noun + verb
