n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [10**10] * n
dp[0] = 0
for i in range(n):
    for j in range(i + 1, min(i + k + 1, n)):
        dp[j] = min(dp[j], dp[i] + abs(h[i] - h[j]))
print(dp[-1])
