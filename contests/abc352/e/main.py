from atcoder.dsu import DSU

n, m = map(int, input().split())
G = DSU(n)
query = []
for _ in range(m):
    k, c = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(k - 1):
        G.merge(a[i] - 1, a[i + 1] - 1)

    query.append([k, c, a])

if G.size(0) != n:
    print(-1)
