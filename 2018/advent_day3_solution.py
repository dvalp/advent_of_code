import numpy as np
import re

def calculate_overlap():
    a = np.zeros([1000,1000])
    with open('/Users/dtv/Downloads/advent-input-day3', 'r') as f:
        rectangles = f.readlines()
    for r in rectangles:
        coords = [int(num) for num in re.split('[@,:x]', r.strip())[1:]]
        a[coords[0]:coords[0]+coords[2], coords[1]:coords[1]+coords[3]] += 1

    print(np.sum(a > 1))

    # print rectangle details for non-overlapping rectangle(s)
    for r in rectangles:
        coords = [int(num) for num in re.split('[@,:x]', r.strip())[1:]]
        if np.all(a[coords[0]:coords[0]+coords[2], coords[1]:coords[1]+coords[3]] == 1):
            print(r)
