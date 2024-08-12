import sys
from functools import cache

n = int(input())
preprev = 1
prev = 1
tmp = 2

for _ in range(3, n):
    tmp, prev, preprev = (tmp + prev) % (10**9 + 7), tmp, prev

print(tmp)
