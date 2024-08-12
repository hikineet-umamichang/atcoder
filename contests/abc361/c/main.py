n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

k = n - k
ans = 10**20
for i in range(n - k + 1):
    ans = min(ans, a[i + k - 1] - a[i])

print(ans)
