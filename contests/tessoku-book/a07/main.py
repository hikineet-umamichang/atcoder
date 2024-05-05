from itertools import accumulate

d = int(input())
n = int(input())
query = [list(map(int, input().split())) for _ in range(n)]

event = [0] * (d + 1)
for i in range(n):
    l, r = query[i]
    event[l - 1] += 1
    event[r] -= 1
ans = list(accumulate(event))
print(*ans[:-1], sep="\n")
