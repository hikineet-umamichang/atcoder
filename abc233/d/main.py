from collections import Counter
from itertools import accumulate

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = accumulate(a)
c = Counter()

c[0] += 1
ans = 0
for x in b:
    y = x - k
    ans += c[y]
    c[x] += 1
print(ans)
