from itertools import product
import numpy as np

class SeatGridB:
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
        return '\n'.join([''.join(row) for row in self.mx])

    def get_nb_dir(self, i, j, rstep, cstep):
        rpos, cpos = rstep, cstep
        while True:
            seat = self[i + rpos, j + cpos]
            if seat == '.':
                if rstep != 0:
                    rpos += rstep
                if cstep != 0:
                    cpos += cstep
            elif seat in ['L', '#']:
                return seat
            else:
                return None

    def get_nbs(self, i, j):
        nbs = [
            self.get_nb_dir(i, j, -1, -1), # NW
            self.get_nb_dir(i, j, -1, 0),  # N
            self.get_nb_dir(i, j, -1, 1),  # NE

            self.get_nb_dir(i, j, 0, -1),  # W
            self.get_nb_dir(i, j, 0, 1),   # E

            self.get_nb_dir(i, j, 1, -1),  # SW
            self.get_nb_dir(i, j, 1, 0),   # S
            self.get_nb_dir(i, j, 1, 1)    # SE
        ]

        return np.array([nb for nb in nbs if nb])

    def eval_seat(self, i, j):
        seat = self.mx[i, j]
        if seat == '.':
            return '.'
        else:
            nbs = self.get_nbs(i, j)
            if seat == 'L':
                return '#' if sum(nbs == '#') == 0 else 'L'
            elif seat == '#':
                return 'L' if sum(nbs == '#') >= 5 else '#'

    def shuffle(self):
        mx_new = np.zeros((self.nrow, self.ncol), dtype=str)
        for i, j in product(range(self.nrow), range(self.ncol)):
            mx_new[i, j] = self.eval_seat(i, j)

        self.mx = mx_new

