import re
from functools import reduce
from string import ascii_lowercase as letters
import numpy as np

raw = open('input.txt', 'r').read().split('\n\n')

def grp_to_distinct(grp):
    grp_strip = re.sub('\s+', '', grp)
    return ''.join(set(grp_strip))

data = [grp_to_distinct(grp) for grp in raw]
total = sum(len(s) for s in data)
print(f"The sum of the counts is: {total}")

# PART B ======================================================================

def q_to_array(q):
    return np.array([letter in q for letter in letters])

groups = [
    [q_to_array(q) for q in group.split()]
    for group in raw
]

groups_reduced = [sum(reduce(lambda a, b: a & b, group)) for group in groups]
total = sum(groups_reduced)
print(f"The sum of the new count is: {total}")
