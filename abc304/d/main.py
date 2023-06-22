w, h = map(int, input().split())
n = int(input())
G = []
for _ in range(n):
    p, q = map(int, input().split())
    G.append([p, q])
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

import collections
import bisect

c = collections.Counter()

for x in G:
    x_h = bisect.bisect_left(a, x[0])
    x_w = bisect.bisect_left(b, x[1])

    c[x_h * 10**10 + x_w] += 1

if len(c) < (A + 1) * (B + 1):
    print(0, c.most_common()[0][1])
else:
    print(c.most_common()[-1][1], c.most_common()[0][1])
