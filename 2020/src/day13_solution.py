from pathlib import Path


def find_bus(target_time: int, schedule: str):
    bus_ids = [int(bus) for bus in schedule.split(",") if bus.isnumeric()]
    wait_time, bus = min((bus - (target_time % bus), bus) for bus in bus_ids)
    return wait_time * bus


if __name__ == '__main__':
    sample_target, sample_schedule = """939
    7,13,x,x,59,x,31,19""".split()
    real_target, real_schedule = Path("../data/input_day13.txt").read_text().split()

    print(find_bus(int(sample_target), sample_schedule))
    print(find_bus(int(real_target), real_schedule))
