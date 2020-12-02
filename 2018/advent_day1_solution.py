from itertools import accumulate, cycle


def get_frequency():
    with open('input_day1', 'r') as f:
        result = sum(int(itm) for itm in f.readlines())

    return result


def find_first_cycle():
    with open('input_day1', 'r') as f:
        inp = [itm.strip() for itm in f.readlines()]

    total = 0
    frequencies = set([total])
    cont = True
    counter = 0
    while cont:
        for op in inp:
            if op[0] == '+':
                total += int(op[1:])
            elif op[0] == '-':
                total -= int(op[1:])
            if total in frequencies:
                result = total
                print(counter + 1)
                cont = False
                return result

            frequencies.add(total)
            counter += 1

    # return result


def find_first_cycle_updated():
    with open('input_day01', 'r') as f:
        inp = [int(itm.strip()) for itm in f.readlines()]

    frequencies = {0}
    return next(f for f in accumulate(cycle(inp)) if f in frequencies or frequencies.add(f))
