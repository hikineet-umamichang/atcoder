from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = list(Counter(a).items())
c.sort()

sm = sum(a)
d = {}
for k, g in c:
    sm -= k * g
    d[k] = sm

ans = [d[x] for x in a]
print(*ans)
