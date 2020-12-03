from functools import reduce

data = [list(line.strip()) for line in open('input.txt', 'r')]


def descend_slope(data, moves_right, moves_down):
    HEIGHT = len(data)
    WIDTH = len(data[0])
    loc_row, loc_col = 0, 0
    ntrees = 0
    while loc_row < HEIGHT:
        if data[loc_row][loc_col] == '#':
            ntrees += 1
        loc_row = loc_row + moves_down
        loc_col = (loc_col + moves_right) % WIDTH
    return ntrees

trees31 = descend_slope(data, 3, 1)
print(f"You encounter {trees31} trees.")

move_sets = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
ntrees = [descend_slope(data, r, d) for r, d in move_sets]
trees_prod = reduce(lambda a, b: a*b, ntrees)

print(f"The product is: {trees_prod}")
