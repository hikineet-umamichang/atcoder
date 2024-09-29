n, k = map(int, input().split())
G = [set() for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)
V = set(map(int, input().split()))

if k == 1:
    exit(print(1))

ans = n
Q = list()
for idx, x in enumerate(G):
    if len(x) == 1:
        Q.append(idx)

for x in Q:
    if x not in V:
        ans -= 1
        b = G[x].pop()
        G[b].remove(x)

        if len(G[b]) == 1:
            Q.append(b)
print(ans)
