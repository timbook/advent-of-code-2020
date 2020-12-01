from itertools import product

report = [int(item) for item in open('input.txt', 'r').readlines()]
dubs = {(a + b): (a, b) for a, b in product(report, report)}

nums = dubs[2020]
prod1 = nums[0]*nums[1]
print(f"Doubles product: {prod1}")

trips = {(a + b + c): (a, b, c) for a, b, c in product(report, report, report)}
nums = trips[2020]
prod2 = nums[0]*nums[1]*nums[2]
print(f"Triples product: {prod2}")
