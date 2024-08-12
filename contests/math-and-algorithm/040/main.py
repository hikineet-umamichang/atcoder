n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = [int(input()) for _ in range(m)]

from itertools import accumulate

c = list(accumulate([0] + a))

ans = 0
for i in range(m - 1):
    ans += abs(c[b[i] - 1] - c[b[i + 1] - 1])
print(ans)
