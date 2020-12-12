from itertools import product
import numpy as np

class SeatGridA:
    def __init__(self, mx):
        self.mx = mx
        self.nrow, self.ncol = self.mx.shape

    @property
    def count(self):
        return sum(sum(self.mx == '#'))

    def __getitem__(self, ix):
        i, j = ix
        if (0 <= i <= self.nrow - 1) and (0 <= j <= self.ncol - 1):
            return self.mx[i, j]
        else:
            return None

    def __repr__(self):
        return '\n'.join([''.join(row) for row in grid.mx])

    def get_neighbors(self, i, j):
        nbs = [
            self[i - 1, j - 1], self[i - 1, j], self[i - 1, j + 1],
            self[i, j - 1], self[i, j + 1],
            self[i + 1, j - 1], self[i + 1, j], self[i + 1, j + 1]
        ]
        return np.array([nb for nb in nbs if nb])

    def eval_seat(self, i, j):
        nbs = self.get_neighbors(i, j)
        seat = self.mx[i, j]
        if seat == 'L':
            return '#' if sum(nbs == '#') == 0 else 'L'
        elif seat == '#':
            return 'L' if sum(nbs == '#') >= 4 else '#'
        else:
            return seat

    def shuffle(self):
        mx_new = np.zeros((self.nrow, self.ncol), dtype=str)
        for i, j in product(range(self.nrow), range(self.ncol)):
            mx_new[i, j] = self.eval_seat(i, j)

        self.mx = mx_new

