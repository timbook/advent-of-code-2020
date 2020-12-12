import math

class Boat:
    def __init__(self):
        self.loc = (0, 0)
        self.dir = (1, 0)

    def move(self, move):
        char = move[0]
        n = int(move[1:])

        if char == 'E':
            self.loc = (self.loc[0] + n, self.loc[1])
        elif char == 'W':
            self.loc = (self.loc[0] - n, self.loc[1])
        elif char == 'N':
            self.loc = (self.loc[0], self.loc[1] + n)
        elif char == 'S':
            self.loc = (self.loc[0], self.loc[1] - n)
        elif char in ['L', 'R']:
            dir_map = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            turns = round(n / 90)
            curr_angle = dir_map.index(self.dir)
            mult = 1 if char == 'L' else -1
            self.dir = dir_map[(curr_angle + mult*turns) % 4]
        elif char == 'F':
            self.loc = (
                self.loc[0] + n*self.dir[0],
                self.loc[1] + n*self.dir[1]
            )

    def dist(self, x, y):
        return abs(self.loc[0] - x) + abs(self.loc[1] - y)

    def __repr__(self):
        return f'Boat({self.loc[0]}, {self.loc[1]})'
