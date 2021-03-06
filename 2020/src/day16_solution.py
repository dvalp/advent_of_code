import itertools
import re
from collections import namedtuple, defaultdict
from operator import itemgetter
from pathlib import Path

from math import prod

sample_text = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".split("\n\n")

RE_VALIDATION = re.compile(r"(?P<field>.*): (?P<range1v1>\d+)-(?P<range1v2>\d+) or (?P<range2v1>\d+)-(?P<range2v2>\d+)")
ParsedDocuments = namedtuple("ParsedDocuments", "validation_rules, valid_numbers, my_ticket, other_tickets")


def parse_documents(input_document: list[str]) -> ParsedDocuments:
    """
    Divide the document in the pieces needed for part 1 and part 2 solutions.

    The input data should be divided into 3 groups, separated by an empty line
    in the original text.

    The validation rules are needed for part 2 only. They consist of filed
    names and the numbers that would be valid values. The valid numbers are
    simply a set of all numbers that would be valid for any rule. My ticket and
    the other tickets are simply a row (tuple) of integers that represent the
    data for one (possibly valid) ticket

    :param input_document: List of strings that represent sections of the data
    :return: Parsed data returned as a namedtuple
    """
    ticket_validation, my_ticket_values, other_tickets_values = input_document

    validation_rules = {}
    for line in ticket_validation.split("\n"):
        match_groups = re.match(RE_VALIDATION, line).groupdict()
        validation_rules[match_groups["field"]] = \
            set(range(int(match_groups["range1v1"]), int(match_groups["range1v2"]) + 1)) | \
            set(range(int(match_groups["range2v1"]), int(match_groups["range2v2"]) + 1))

    valid_numbers = set(itertools.chain.from_iterable(validation_rules.values()))

    my_ticket = tuple(int(val) for val in my_ticket_values.split("\n")[1].split(","))

    other_tickets = []
    for line in other_tickets_values.strip().split("\n")[1:]:
        other_tickets.append(tuple(int(val) for val in line.split(",")))

    return ParsedDocuments(validation_rules, valid_numbers, my_ticket, other_tickets)


def validate_tickets(other_tickets: list[tuple[int]], valid_numbers: set[int]) -> tuple[int, list[tuple[int]]]:
    """
    The part one solution consists of the sum of all values that would be
    invalid for any possible field.

    Part 2 requires only the valid tickets, those filters for those, as well.

    :param other_tickets: All tickets that were scanned
    :param valid_numbers: All values that would valid for a field
    :return: The total of the invalid numbers, and the valid tickets.
    """
    total_invalid = 0
    valid_tickets = []
    for ticket in other_tickets:
        if invalid := (set(ticket) - valid_numbers):
            total_invalid += sum(invalid)
        else:
            valid_tickets.append(ticket)

    return total_invalid, valid_tickets


def get_positions(tickets: list[tuple[int]], validation_rules: dict[str, set[int]]) -> dict[str, int]:
    """
    Most values could be valid for a number of different fields. Here we
    eliminate duplicates to find the true name for each field.

    :param tickets: List of all tickets to use for analysis
    :param validation_rules: Rules to use for predicting field names
    :return: Dict of true values mapped to their field index
    """
    ticket_fields = [set(column) for column in zip(*tickets)]
    potential_names = [[key for key, values in validation_rules.items() if field.issubset(values)]
                       for field in ticket_fields]
    possible_positions = defaultdict(set)
    for idx, fields in enumerate(potential_names):
        for field in fields:
            possible_positions[field].add(idx)

    true_positions = {}
    to_remove = set()
    for field_name, positions in sorted(possible_positions.items(), key=itemgetter(1)):
        position = next(iter(positions - to_remove))
        true_positions[field_name] = position
        to_remove.add(position)

    return true_positions


if __name__ == '__main__':
    input_text = Path("../data/input_day16.txt").read_text().split("\n\n")

    sample_docs = parse_documents(sample_text)
    print(validate_tickets(sample_docs.other_tickets, sample_docs.valid_numbers))

    real_docs = parse_documents(input_text)
    total_valid, validated_tickets = validate_tickets(real_docs.other_tickets, real_docs.valid_numbers)
    validated_tickets.append(real_docs.my_ticket)
    print(total_valid)

    field_positions = get_positions(validated_tickets, real_docs.validation_rules)
    field_idxs = [idx for key, idx in field_positions.items() if key in
                  {'departure time', 'departure station', 'departure platform', 'departure date', 'departure location',
                   'departure track'}]
    print(prod(real_docs.my_ticket[idx] for idx in field_idxs))
