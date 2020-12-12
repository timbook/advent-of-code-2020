data = sorted([int(line) for line in open('input.txt', 'r')])
data = [0] + data + [max(data) + 3]

diffs = [b - a for a, b in zip(data[:-1], data[1:])]

n1, n3 = diffs.count(1), diffs.count(3)
print(f"Joltage product = {n1*n3}")

# PART B =====================================================================

scores = {}
datar = data[::-1]
for i, n in enumerate(datar):
    next_nums = datar[:i][-3:]

    if not next_nums:
        scores[n] = 1
        continue

    scores[n] = 0
    for next_num in next_nums:
        is_valid = next_num - n <= 3
        if is_valid:
            scores[n] += scores[next_num]

print(f"Valid Combos: {scores[0]}")
