from atcoder.segtree import SegTree

n, k = map(int, input().split())
p = list(map(int, input().split()))

pp = []
for idx, i in enumerate(p):
    pp.append([i, idx])
pp.sort()

q = []
for x in pp:
    q.append(x[1])


G_max = SegTree(max, -(10**20), q)
G_min = SegTree(min, 10**20, q)

ans = 10**20
for i in range(n - k + 1):
    mx = G_max.prod(i, i + k)
    mn = G_min.prod(i, i + k)
    ans = min(abs(mx - mn), ans)
print(ans)
