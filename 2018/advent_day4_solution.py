import re
from collections import defaultdict, Counter

def find_sleeper():
    with open('/Users/dtv/Downloads/advent-input-day4', 'r') as f:
        schedule = sorted(f.readlines())
    
    guards = defaultdict(Counter)
    guard_id = -1
    start_pos = -1

    for rec in schedule:
        if "begins shift" in rec:
            guard_id = int(re.search('#(\d+)', rec).groups()[0])
        elif "falls asleep" in rec:
            split_point = rec.find("]")
            start_pos = int(rec[split_point-2:split_point])
        elif "wakes up" in rec:
            end_pos = int(rec[split_point-2:split_point])
            guards[guard_id].update(range(start_pos, end_pos))

    longest_max_id = -1
    longest_max_minute = -1
    longest_max_time = -1
    for gid in guards:
        total_sleep = sum(guards[gid].values())
        minute, count = guards[gid].most_common(1)[0]
        if total_sleep > longest_max_time:
            longest_max_id = gid
            longest_max_minute = minute
            longest_max_time = total_sleep

    first_id =  longest_max_id * longest_max_minute

    most_max_id = -1
    most_max_minute = -1
    most_max_time = -1
    for gid in guards:
        total_sleep = sum(guards[gid].values())
        minute, count = guards[gid].most_common(1)[0]
        if count > most_max_time:
            most_max_id = gid
            most_max_minute = minute
            most_max_time = count
            
    second_id = most_max_id * most_max_minute

    return first_id, second_id

