n = int(input())
a = [[0] * (n) for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j, x in enumerate(tmp):
        a[i][j] = x
        a[j][i] = x

ans = 1
for i in range(n):
    x, y = min(ans, i + 1), max(ans, i + 1)
    ans = a[x - 1][y - 1]
print(ans)
