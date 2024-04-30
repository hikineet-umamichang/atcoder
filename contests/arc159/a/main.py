from collections import deque

n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

b = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            b[i][j] = 1


def bfs(s, t, m):
    # 最短閉路
    if s == t:
        mn = 10**12
        for i in range(len(b[s])):
            if i != s:
                tmp = bfs(s, i, m)
                if tmp == -1:
                    tmp += 10**12
                mn = min(tmp, mn)
        return mn + m + 1

    dist = [-1] * n
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in b[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            que.append(w)
    return dist[t]


q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    m = abs(s - t) // n-1
    s = (s - 1) % n
    t = (t - 1) % n

    if a[s][t] == 1:
        print(1)
    elif sum(b[s]) == 0:
        print(-1)
    else:
        print(bfs(s, t, m))
