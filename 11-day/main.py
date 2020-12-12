from itertools import product
import numpy as np

from seats_a import SeatGridA
from seats_b import SeatGridB

# PART A ======================================================================

mx = np.array([list(line) for line in open('input.txt', 'r')])

grida = SeatGridA(mx)

cache = [grida.count]
while True:
    grida.shuffle()
    cache.append(grida.count)
    if len(cache) >= 3 and all(c == cache[-1] for c in cache[-3:]):
        break

n_stable = cache[-1]
print(f"A :: After stabilizing, there are {n_stable} occupied seats.")

# PART B ======================================================================

gridb = SeatGridB(mx)

cache = [gridb.count]
while True:
    gridb.shuffle()

    cache.append(gridb.count)
    if len(cache) >= 3 and all(c == cache[-1] for c in cache[-3:]):
        break

n_stable = cache[-1]
print(f"B :: After stabilizing, there are {n_stable} occupied seats.")
