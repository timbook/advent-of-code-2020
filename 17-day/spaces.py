from itertools import product
import numpy as np

class Space3D:
    def __init__(self, raw):
        middle_plane_str = np.array([list(line) for line in raw.split('\n')])
        middle_plane = np.where(middle_plane_str == '#', 1, 0)
        nrow, ncol = middle_plane.shape
        mx = np.zeros((nrow, ncol, 3), dtype=int)
        mx[:, :, 1] = middle_plane
        self.mx = np.pad(mx, 7)

    @property
    def count(self):
        return np.sum(self.mx)

    def center_slice(self):
        mx_int = self.mx[:, :, 7]
        mx_str = np.where(mx_int == 1, '#', '.')
        print('\n'.join([''.join(line) for line in mx_str]))

    def get_nbs(self, i, j, k):
        mx_out = self.mx[
            max(i - 1, 0):(i + 2),
            max(j - 1, 0):(j + 2),
            max(k - 1, 0):(k + 2)
        ].copy()
        mx_out[1, 1, 1] = 0
        return mx_out

    def cycle(self):
        nx, ny, nz = self.mx.shape
        new_mx = self.mx.copy()
        for i, j, k in product(range(nx), range(ny), range(nz)):
            nbs = np.sum(self.get_nbs(i, j, k))
            if self.mx[i, j, k] == 1:
                new_val = 1 if (2 <= nbs <= 3) else 0
            else:
                new_val = 1 if (nbs == 3) else 0
            new_mx[i, j, k] = new_val
        self.mx = new_mx

class Space4D:
    def __init__(self, raw):
        middle_plane_str = np.array([list(line) for line in raw.split('\n')])
        middle_plane = np.where(middle_plane_str == '#', 1, 0)
        nrow, ncol = middle_plane.shape
        mx = np.zeros((nrow, ncol, 3, 3), dtype=int)
        mx[:, :, 1, 1] = middle_plane
        self.mx = np.pad(mx, 7)

    @property
    def count(self):
        return np.sum(self.mx)

    def get_nbs(self, i, j, k, l):
        mx_out = self.mx[
            max(i - 1, 0):(i + 2),
            max(j - 1, 0):(j + 2),
            max(k - 1, 0):(k + 2),
            max(l - 1, 0):(l + 2),
        ].copy()
        mx_out[1, 1, 1, 1] = 0
        return mx_out

    def cycle(self):
        nx, ny, nz, nw = self.mx.shape
        new_mx = self.mx.copy()
        for i, j, k, l in product(range(nx), range(ny), range(nz), range(nw)):
            nbs = np.sum(self.get_nbs(i, j, k, l))
            if self.mx[i, j, k, l] == 1:
                new_val = 1 if (2 <= nbs <= 3) else 0
            else:
                new_val = 1 if (nbs == 3) else 0
            new_mx[i, j, k, l] = new_val
        self.mx = new_mx
