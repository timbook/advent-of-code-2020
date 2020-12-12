from boat import Boat
from waypoint import Waypoint

# PART A ======================================================================

boat = Boat()

#  moves = ['F10', 'N3', 'F7', 'R90', 'F11']
moves = open('input.txt', 'r').readlines()
for move in moves:
    boat.move(move)

d = boat.dist(0, 0)
print(f"A :: Distance to origin: {d}")

# PART B ======================================================================

way = Waypoint()
for move in moves:
    way.move(move)

d = way.dist()
print(f"B :: Distance to origin: {d}")
