from spaces import Space3D, Space4D

raw = """#....#.#
..##.##.
#..#..#.
.#..#..#
.#..#...
##.#####
#..#..#.
##.##..#"""

space = Space3D(raw)
for _ in range(6):
    space.cycle()

print(f"A :: After 6 cycles in 3D: {space.count}")

space = Space4D(raw)
for _ in range(6):
    space.cycle()

print(f"B :: After 6 cycles in 4D: {space.count}")
