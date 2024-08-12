n, q = map(int, input().split())
a = list(map(int, input().split()))
lr = [list(map(int, input().split())) for _ in range(q)]

from itertools import accumulate

b = list(accumulate([0] + a))

for l, r in lr:
    print(b[r] - b[l - 1])
