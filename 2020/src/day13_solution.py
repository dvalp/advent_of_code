from pathlib import Path


def find_bus(target_time: int, schedule: str) -> int:
    bus_ids = [int(bus) for bus in schedule if bus.isnumeric()]
    wait_time, bus = min((bus - (target_time % bus), bus) for bus in bus_ids)
    return wait_time * bus


def gold_challenge(schedule) -> int:
    bus_ids = [int(bus) for bus in schedule if bus.isnumeric()]
    time_offsets = [schedule.index(str(bus)) for bus in bus_ids]
    id_offsets = list((zip(bus_ids, time_offsets)))
    max_id, max_id_offset = max(zip(bus_ids[1:], time_offsets[1:]))
    reference_id = bus_ids[0]

    max_id_time = max_id
    while (max_id_time - max_id_offset) % reference_id != 0:
        max_id_time += max_id

    timestamp = max_id_time - max_id_offset
    while not validate_timestamp(timestamp, id_offsets):
        timestamp += reference_id * max_id

    return timestamp


def validate_timestamp(timestamp: int, id_offsets: list[tuple[int, int]]) -> bool:
    return timestamp % id_offsets[0][0] == 0 and all((bus - (timestamp % bus) == offset) for bus, offset in id_offsets[1:])


if __name__ == '__main__':
    sample_target, sample_schedule = """939
    7,13,x,x,59,x,31,19""".split()
    real_target, real_schedule = Path("../data/input_day13.txt").read_text().split()
    sample_schedule = sample_schedule.split(",")
    real_schedule = real_schedule.split(",")

    print(find_bus(int(sample_target), sample_schedule))
    print(find_bus(int(real_target), real_schedule))

    print(gold_challenge(sample_schedule))
    print(gold_challenge(real_schedule))
