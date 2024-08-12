h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

row = [sum(x) for x in a]
col = [0] * w
for i in range(h):
    for j in range(w):
        col[j] += a[i][j]

ans = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] = row[i] + col[j] - a[i][j]

for x in ans:
    print(*x)
