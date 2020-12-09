import numpy as np

#  raw = """35
#  20
#  15
#  25
#  47
#  40
#  62
#  55
#  65
#  95
#  102
#  117
#  150
#  182
#  127
#  219
#  299
#  277
#  309
#  576"""

#  nums = [int(i) for i in raw.split('\n')]
#  pre = 5

nums = [int(i) for i in open('input.txt', 'r')]
pre = 25

def lookback_sum(vec, n):
    lookup = [False]*(n + 1)
    for i in vec:
        if i >= n:
            continue

        if lookup[n - i]:
            return True
        else:
            lookup[i] = True

    return False

def find_invalid_number(nums, pre):
    for i, n in enumerate(nums):

        if i < pre:
            continue

        if not lookback_sum(nums[(i - pre):i], n):
            return n

enc_num = find_invalid_number(nums, pre)
print(f"Encryption number: {enc_num}")

vec = np.cumsum(nums)
for i, n in enumerate(vec):
    subvec = vec[(i + 1):] - vec[i]
    if enc_num in subvec:
        loc = i + 1 + np.where(subvec == enc_num)[0][0]
        start, end = i + 1, loc
        break

weakness = max(nums[start:end]) + min(nums[start:end])
print(f"Encryption weakness: {weakness}")
