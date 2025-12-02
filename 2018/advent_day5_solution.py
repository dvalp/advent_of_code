import string
from collections import Counter
"""
xLoad Sequence
xmake letter pairs
replace all pairs
cycle through list until no changes
check string length before and after cycle to detect changes
return remaining sequence
"""

def sequence_reactions():
    with open('/Users/dtv/Downloads/advent-input-day5', 'r') as f:
        original_sequence = f.read().strip()

    pairs = set()
    for pair in list(zip(string.ascii_lowercase,string.ascii_uppercase)):
        pairs.add(''.join(pair))
        pairs.add(''.join(pair[::-1]))

    reduced_sequence = perform_reactions(original_sequence, pairs)

    # Try removing a letter and see if it improves the sequence reduction
    letter_improvements = Counter()
    for letter in string.ascii_uppercase:
        letter_sequence = perform_reactions(original_sequence.replace(letter, '').replace(letter.lower(), ''), pairs)
        letter_improvements[letter] = len(letter_sequence)

    return len(reduced_sequence), letter_improvements

def perform_reactions(sequence, pairs):
    replaced = True
    while replaced:
        replaced = False
        start_length = len(sequence)
        for pair in pairs:
            sequence = sequence.replace(pair, '')
        if len(sequence) < start_length:
            replaced = True
    return sequence
