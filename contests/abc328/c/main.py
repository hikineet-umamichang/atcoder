n, q = map(int, input().split())
s = input()
lr = [list(map(int, input().split())) for _ in range(q)]

ss = [0] * n
for i in range(n - 1):
    if s[i] == s[i + 1]:
        ss[i] += 1

from itertools import accumulate

ss = [0] + list(accumulate(ss))
for l, r in lr:
    print(ss[r - 1] - ss[l - 1])
# print(*ss)
