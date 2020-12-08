RAW = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

parsed_codes = [line.split() for line in RAW.split("\n")]


def find_loop(instructions: list[list[str, str]], edit=None):
    position = 0
    accumulator = 0
    visited = set()
    while True:
        visited.add(position)
        command = instructions[position][0]
        value = int(instructions[position][1])
        prev_pos = (command, position)

        if edit and position == edit[1]:
            command = "nop" if command == "jmp" else "jmp"

        if command == "nop":
            position += 1
        elif command == "acc":
            accumulator += value
            position += 1
        elif command == "jmp":
            position += value

        if position in visited:
            return "fail", accumulator, prev_pos
        elif position >= len(instructions):
            return accumulator, prev_pos


if __name__ == '__main__':
    print(find_loop(parsed_codes))

    with open("../data/input_day08.txt", "r") as f:
        instruction_codes = [line.strip().split() for line in f]

    edits = {('nop', 72), ('jmp', 440), ('jmp', 122), ('jmp', 250), ('jmp', 369), ('jmp', 570), ('jmp', 42), ('nop', 458), ('jmp', 170), ('jmp', 298), ('nop', 476), ('jmp', 243), ('nop', 131), ('jmp', 35), ('jmp', 99), ('nop', 167), ('jmp', 410), ('nop', 560), ('jmp', 220), ('jmp', 339), ('jmp', 284), ('jmp', 293), ('jmp', 76), ('jmp', 21), ('jmp', 268), ('jmp', 277), ('jmp', 460), ('jmp', 405), ('nop', 409), ('jmp', 524), ('jmp', 469), ('jmp', 588), ('jmp', 240), ('jmp', 359), ('jmp', 304), ('jmp', 423), ('jmp', 551), ('jmp', 69), ('jmp', 142), ('nop', 265), ('nop', 210), ('jmp', 96), ('jmp', 334), ('nop', 338), ('nop', 283), ('nop', 176), ('jmp', 489), ('jmp', 62), ('nop', 11), ('jmp', 71), ('nop', 276), ('jmp', 519), ('jmp', 226), ('jmp', 592), ('jmp', 601), ('jmp', 0), ('nop', 187), ('jmp', 9), ('jmp', 73), ('jmp', 137), ('jmp', 27), ('jmp', 576), ('jmp', 347), ('jmp', 112), ('jmp', 313), ('jmp', 267), ('nop', 518), ('jmp', 413), ('jmp', 50), ('jmp', 477), ('jmp', 178), ('jmp', 13), ('jmp', 132), ('nop', 310), ('jmp', 214), ('nop', 575), ('jmp', 397), ('jmp', 470), ('jmp', 235), ('jmp', 299), ('jmp', 6), ('jmp', 363), ('jmp', 189), ('jmp', 79), ('jmp', 198), ('jmp', 564), ('nop', 95), ('jmp', 463), ('jmp', 356), ('jmp', 182), ('nop', 225), ('nop', 408), ('jmp', 230)}
    for comm in edits:
        print(find_loop(instruction_codes, comm))
