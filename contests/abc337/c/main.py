n = int(input())
a = list(map(int, input().split()))

d = {}

for idx, i in enumerate(a):
    d[i] = idx + 1

ans = [0] * n
ans[0] = a.index(-1) + 1

for i in range(1, n):
    ans[i] = d[ans[i - 1]]

print(*ans)
