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


def parse_documents(input_document):
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


def validate_tickets(other_tickets, valid_numbers) -> tuple[int, list[tuple[int]]]:
    total_invalid = 0
    valid_tickets = []
    for ticket in other_tickets:
        if invalid := (set(ticket) - valid_numbers):
            total_invalid += sum(invalid)
        else:
            valid_tickets.append(ticket)

    return total_invalid, valid_tickets


def get_positions(tickets, validation_rules):
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

    positions = get_positions(validated_tickets, real_docs.validation_rules)
    field_idxs = [idx for key, idx in positions.items() if key in
                  {'departure time', 'departure station', 'departure platform', 'departure date', 'departure location',
                   'departure track'}]
    print(prod(real_docs.my_ticket[idx] for idx in field_idxs))
