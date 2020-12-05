def pass_to_rc(s):
    row_raw = s[:7]
    col_raw = s[7:]
    row = int('0b' + row_raw.replace('F', '0').replace('B', '1'), 2)
    col = int('0b' + col_raw.replace('L', '0').replace('R', '1'), 2)
    return row, col

data = [pass_to_rc(line.strip()) for line in open('input.txt', 'r')]
seat_id = [8*r + c for r, c in data]
max_id = max(seat_id)
print(f"The maximum seat ID is: {max_id}")

min_id = min(seat_id)
missing_id = list(set(range(min_id, max_id + 1)) - set(seat_id))[0]
print(f"My seat ID is: {missing_id}")
