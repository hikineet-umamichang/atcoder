from atcoder.dsu import DSU

n, q = map(int, input().split())
G = DSU(n)
for i in range(q):
    t, u, v = map(int, input().split())

    if t:
        print(1 if G.same(u, v) else 0)
    else:
        G.merge(u, v)
