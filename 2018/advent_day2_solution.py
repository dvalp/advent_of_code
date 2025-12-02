
two_counts = 0
three_counts = 0
for s in inp:
    counts = Counter(s)
    if 2 in counts.values():
        two_counts +=1
    if 3 in counts.values():
        three_counts += 1
chk = two_counts * three_counts

for first in inp:
    for second in inp:
        matched = ''.join(pair[0] for pair in zip(first, second) if pair[0] == pair[1])
        if (len(first) - len(matched)) == 1:
            print(matched)
