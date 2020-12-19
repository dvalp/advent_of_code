import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import TypedDict, Optional

SAMPLE_INPUT = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

REPLACEMENT_RULES = """8: 42 | 42 8
11: 42 31 | 42 11 31"""


class Rule(TypedDict):
    value: Optional[int]
    rules: Optional[list[list[int]]]


@dataclass
class ResolveRules:
    rule_defs: dict[int, Rule] = field(default_factory=dict)
    messages: list[str] = field(default_factory=list)
    re_pattern: Optional[re.Pattern] = None

    @property
    def valid_count(self):
        return sum(1 for message in self.messages if self.re_pattern.match(message))

    def add_rule(self, rule: str):
        left, right = rule.split(": ")
        key = int(left)
        if '"' in right:
            self.rule_defs[key] = Rule(value=right[1:-1], rules=None)
        else:
            rules = [[int(val) for val in group.split()] for group in right.split(" | ")]
            self.rule_defs[key] = Rule(value=None, rules=rules)

    def import_data(self, raw_data: str):
        raw_rules, raw_messages = raw_data.split("\n\n")
        for rule in raw_rules.split("\n"):
            self.add_rule(rule)
        self.messages = raw_messages.strip().split()

    def build_pattern(self, rule_id: int = 0):
        message_pattern = self._build_pattern(rule_id)
        self.re_pattern = re.compile(rf"^{message_pattern}$")

    def _build_pattern(self, rule_id: int, depth: int = 0):
        current_rule = self.rule_defs[rule_id]
        if letter := current_rule["value"]:
            return letter

        groups = []
        for group in current_rule["rules"]:
            group_pieces = []
            for new_id in group:
                if new_id == rule_id:
                    if depth < 5:
                        group_pieces.append(self._build_pattern(new_id, depth=depth + 1))
                else:
                    group_pieces.append(self._build_pattern(new_id, depth=depth))
            groups.append("".join(group_pieces))

        return rf'({"|".join(groups)})'


if __name__ == '__main__':
    challenge_text = Path("../data/input_day19.txt").read_text().strip()
    resolver = ResolveRules()
    resolver.import_data(challenge_text)
    resolver.build_pattern()
    print(resolver.valid_count)

    for rule in REPLACEMENT_RULES.split("\n"):
        resolver.add_rule(rule)
    resolver.build_pattern()
    print(resolver.valid_count)
