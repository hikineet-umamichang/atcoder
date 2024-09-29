from collections import deque, defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        path = []
        while self.parents[x] >= 0:
            path.append(x)
            x = self.parents[x]
        for node in path:
            self.parents[node] = x
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.parents[x_root] > self.parents[y_root]:
            x_root, y_root = y_root, x_root
        self.parents[x_root] += self.parents[y_root]
        self.parents[y_root] = x_root

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


n, m = map(int, input().split())
uvw = [tuple(map(int, input().split())) for _ in range(m)]

adj = [[] for _ in range(n)]
uf = UnionFind(n)
for x, y, z in uvw:
    x -= 1
    y -= 1
    adj[x].append((y, z))
    adj[y].append((x, -z))
    uf.union(x, y)

roots = uf.roots()


def SPFA(roots):
    INF = float("inf")
    dist = [INF] * n
    inqueue = [False] * n
    count = [0] * n
    q = deque()

    for root in roots:
        dist[root] = 0
        q.append(root)
        inqueue[root] = True

    while q:
        u = q.popleft()
        inqueue[u] = False
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                count[v] += 1
                if count[v] >= n:
                    return -1
                if not inqueue[v]:
                    q.append(v)
                    inqueue[v] = True
    return dist


result = SPFA(roots)
if result == -1:
    print(-1)
else:
    print(*result)
