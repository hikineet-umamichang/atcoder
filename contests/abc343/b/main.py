n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ans = [[] for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] == 1:
            ans[i].append(j + 1)
            ans[j].append(i + 1)

for x in ans:
    x.sort()
    print(*x)
print()
