import math

class Waypoint:
    def __init__(self):
        self.loc = (10, 1)
        self.boat = (0, 0)

    def __repr__(self):
        return f"Waypoint{self.loc} :: Boat{self.boat}"

    def move(self, move):
        char, n = move[0], int(move[1:])
        if char == 'N':
            self.loc = (self.loc[0], self.loc[1] + n)
        elif char == 'S':
            self.loc = (self.loc[0], self.loc[1] - n)
        elif char == 'E':
            self.loc = (self.loc[0] + n, self.loc[1])
        elif char == 'W':
            self.loc = (self.loc[0] - n, self.loc[1])
        elif char in ['L', 'R']:
            angle = n if char == 'L' else 360 - n

            # Location relative to boat
            x = self.loc[0]
            y = self.loc[1]

            sinT = round(math.sin(angle * math.pi / 180))
            cosT = round(math.cos(angle * math.pi / 180))

            new_x = x*cosT - y*sinT
            new_y = x*sinT + y*cosT

            self.loc = (new_x, new_y)
        elif char == 'F':
            self.boat = (
                self.boat[0] + n*self.loc[0],
                self.boat[1] + n*self.loc[1]
            )

    def dist(self, x=0, y=0):
        return abs(self.boat[0] - x) + abs(self.boat[1])
