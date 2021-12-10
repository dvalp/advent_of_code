from collections import defaultdict
from pathlib import Path

SAMPLE_DATA = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".strip().split("\n")


def count_simple(input_data):
    number_count = 0
    for line in input_data:
        digits, codes = line.split("|")

        for code in codes.split():
            if len(code) in {2, 3, 4, 7}:
                number_count += 1

    return number_count


def signal_evaluation(input_data) -> int:
    """
    Known: 1, 4, 7, 8
    len 5
        2: not 1, 4, 7, 8 - 3 different from 6
        3: 1, 7, not 4, 8
        5: not 1, 4, 7, 8 - 1 different from 6
    len 6
        0: not superset of 4
        6: not superset of 1
        9: superset of 4

    :param input_data:
    :return:
    """
    result = 0

    for line in input_data:
        digits, codes = line.split("|")
        code_map = map_digits(digits.split())
        result += int("".join(str(code_map[frozenset(code)]) for code in codes.split()))

    return result


def map_digits(digits: list[str]) -> dict[frozenset, int]:
    code_map = {}
    length_map = defaultdict(list)

    for entry in digits:
        length_map[len(entry)].append(frozenset(entry))

    for entry in digits:
        code_map[1] = length_map[2][0]
        code_map[4] = length_map[4][0]
        code_map[7] = length_map[3][0]
        code_map[8] = length_map[7][0]

    for entry in length_map[6]:
        if entry > code_map[4]:
            code_map[9] = entry
        elif not entry > code_map[1]:
            code_map[6] = entry
        else:
            code_map[0] = entry

    for entry in length_map[5]:
        if len(entry ^ code_map[9]) > 1:
            code_map[2] = entry
        elif entry < code_map[6]:
            code_map[5] = entry
        else:
            code_map[3] = entry

    return {value: key for key, value in code_map.items()}


if __name__ == '__main__':
    file_data = Path("../data/input_day08.txt").read_text().strip().split("\n")
    print(count_simple(SAMPLE_DATA))
    print(count_simple(file_data))
    print(signal_evaluation(SAMPLE_DATA))
    print(signal_evaluation(file_data))
