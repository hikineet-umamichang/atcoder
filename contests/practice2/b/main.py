from atcoder.fenwicktree import FenwickTree

n, q = map(int, input().split())
bit = FenwickTree(n)
a = list(map(int, input().split()))
for idx, x in enumerate(a):
    bit.add(idx, x)

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        p, x = query[1], query[2]
        bit.add(p, x)
    else:
        l, r = query[1], query[2]
        bit.sum(l, r)
