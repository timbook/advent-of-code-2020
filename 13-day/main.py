import numpy as np

time = 939
bus_str = '7,13,x,x,59,x,31,19'

#  time, bus_str = open('input.txt', 'r').readlines()
#  time = int(time.strip())

# PART A ======================================================================

bus = [int(n) for n in bus_str.strip().split(',') if n.isdigit()]

bus_div = [time // n + 1 for n in bus]

bus_prod = np.array([b*d - time for b, d in zip(bus, bus_div)])

ix = np.argmin(bus_prod)
prod = bus_prod[ix]*bus[ix]
print(f"Solution product = {prod}")

# PART B ======================================================================

sched = [(i, int(n)) for i, n in enumerate(bus_str.strip().split(',')) if n != 'x']
