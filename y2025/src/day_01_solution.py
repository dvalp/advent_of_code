from pathlib import Path


def unlock(rotations: list[str], start: int = 50) -> tuple[int, int]:
    """
    Calculate code based on rotation combinations.
    Args:
        rotations: Collection of rotation instructions
        start: Starting point for rotations

    Returns:
        Password created from rotation combinations
    """
    position = start
    code1 = 0
    code2 = 0

    for rotation in rotations:
        if rotation.startswith("L"):
            prior_position = position
            position -= int(rotation[1:])
            zero_count = (position // 100) * -1
            if prior_position == 0:
                zero_count -= 1
            if position == 0:
                zero_count += 1
            if position != 0 and position % 100 == 0:
                zero_count += 1
            code2 += zero_count

        elif rotation.startswith("R"):
            position += int(rotation[1:])
            code2 += position // 100
        else:
            raise ValueError(f"Invalid rotation instruction: {rotation}")

        position %= 100
        if position == 0:
            code1 += 1
    return code1, code2


if __name__ == "__main__":
    file_data = Path("y2025/data/input_day_01.txt").read_text().strip().splitlines()
    result1, result2 = unlock(file_data)
    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")
