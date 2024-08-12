n = int(input())
a = [0, 0] + list(map(int, input().split()))
b = [0, 0, 0] + list(map(int, input().split()))

dp = [10**10] * (n + 1)
dp[1] = 0
dp[2] = dp[1] + a[2]

for i in range(3, n + 1):
    dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i])

print(dp[-1])
