n, k = map(int, input().split())
a = list(map(int, input().split()))

import itertools

b = list(itertools.accumulate(a))

import collections

c = collections.Counter()
c[0] += 1
ans = 0
print(b)
for i in range(n):
    ans += c[b[i] - k]
    c[b[i]] += 1
    print(c)
print(ans)
