import string
from collections import deque


def instruction_path():
    with open('/Users/dtv/Downloads/advent-input-day7', 'r') as f:
        steps = [(line[5], line[-13]) for line in f]

    first, second = map(set, zip(*steps))
    start = sorted([step for step in first if step not in second], reverse=True)

    instructions = start.copy()
    plan = list(instructions.pop())
    instructions.extend(step[1] for step in steps if step[0] == plan[0])

    while instructions:
        instructions = sorted(set(instructions))
        for next_step in instructions:
            preconditions = all((code in plan) for code in [step[0] for step in steps if step[1] == next_step])
            if preconditions or (next_step in start):
                plan.append(next_step)
                instructions.remove(next_step)
                instructions.extend(step[1] for step in steps if step[0] == next_step)
                break

    return ''.join(plan)


def instruction_parallel_path():
    with open('/Users/dtv/Downloads/advent-input-day7', 'r') as f:
        steps = [(line[5], line[-13]) for line in f]

    first, second = map(set, zip(*steps))

    start = sorted([step for step in first if step not in second], reverse=True)
    end = sorted(step for step in second if step not in first)

    time_value = {code: value+60 for value, code in enumerate(string.ascii_uppercase, 1)}

    plan = []
    jobs = start[:5]
    instructions = start[5:]

    cycle_count = 0
    while end[0] not in plan:
        cycle_count += 1

        # process jobs
        for job in jobs:
            time_value[job] -= 1
            if time_value[job] == 0:
                jobs.remove(job)
                plan.append(job)
                instructions.extend(step[1] for step in steps if step[0] == job)

        # add new jobs
        instructions = sorted(set(instructions))
        for next_step in instructions:
            if len(jobs) < 5:
                # All preconditions must have completed
                preconditions = all((code in plan) for code in [step[0] for step in steps if step[1] == next_step])
                if preconditions or (next_step in start):
                    instructions.remove(next_step)
                    jobs.append(next_step)

    return cycle_count, time_value
