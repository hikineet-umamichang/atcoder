n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
seen = [False] * n
ans = []
checked = 0


def bfs(tmp):
    global checked
    seen[tmp] = True
    if len(G[tmp]) > 2:
        ans.append(len(G[tmp]))
        checked += len(G[tmp]) + 1
    for x in G[tmp]:
        try:
            if not seen[x]:
                bfs(x)
        except:
            continue


bfs(1)

level2 = [2] * ((n - checked) // 3)
ans.extend(level2)

print(*sorted(ans))
