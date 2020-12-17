import re

pattern = "(\w+)\s?(\w+): (\d)+-(\d+) or (\d)+-(\d+)"
lines = [line.strip() for line in open('input.txt', 'r') if re.match(pattern, line)]

conds = sum([re.findall("(\d+-\d+)", line) for line in lines], [])
tickets = open('input.txt', 'r').readlines()[25:]

def in_range_n(n):
    def inner(cond):
        bounds = cond.split('-')
        lb = int(bounds[0])
        ub = int(bounds[1])
        return lb <= n <= ub
    return inner

def is_valid(n):
    in_range = in_range_n(n)
    return any(in_range(cond) for cond in conds)

def validity_score(ticket):
    return sum([int(n) for n in ticket.strip().split(',') if not is_valid(int(n))])

score = sum([validity_score(t) for t in tickets])
print(f"Ticket scanning error rate: {score}")

valids = [ticket.strip() for ticket in tickets if validity_score(ticket) == 0]
str_to_tup = lambda s: (int(s.split('-')[0]), int(s.split('-')[1]))
cond_map = {
    re.findall('(.*):', line)[0]: str_to_tup(re.findall('(\d+-\d+)', line)[0])
    for line in lines
}
p = len(cond_map)

firsts = [int(v.split(',')[0]) for v in valids]

def all_ok(vec, bounds):
    return all(bounds[0] <= v <= bounds[1] for v in vec)
a = [k for k, v in cond_map.items() if all_ok(firsts, v)]
