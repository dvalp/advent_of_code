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
        code_map = defaultdict(int)
        # for entry in digits.split():
        #     entry_length = len(entry)
        #     match entry_length:
        #         case 2:
        #             code_map[entry] = 1
        #         case 4:
        #             code_map[entry] = 4
        #         case 3:
        #             code_map[entry] = 7
        #         case 7:
        #             code_map[entry] = 8

        for code in codes.split():
            if len(code) in {2, 3, 4, 7}:
                number_count += 1

    return number_count


if __name__ == '__main__':
    file_data = Path("../data/input_day08.txt").read_text().strip().split("\n")
    print(count_simple(SAMPLE_DATA))
    print(count_simple(file_data))
