n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

ans = set()

for i in range(m):
    for j in range(n - 1):
        tmp = a[i][j : j + 2]
        num = max(tmp) * 1000 + min(tmp)
        ans.add(num)

print(n * (n - 1) // 2 - len(ans))
