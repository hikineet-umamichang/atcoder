n = int(input())
dishes = []
for _ in range(n):
    x, y = map(int, input().split())
    dishes.append([x, y])

dp = [[float("inf") * -1, float("inf") * -1] for _ in range(n)]

if dishes[0][0] == 0:
    dp[0] = [max(0, dishes[0][1]), 0]
else:
    dp[0] = [0, max(dishes[0][1], 0)]

for i in range(1, n):
    if dishes[i][0] == 0:
        dp[i][0] = max(max(dp[i - 1][0], dp[i - 1][1]) + dishes[i][1], dp[i - 1][0])
        dp[i][1] = dp[i - 1][1]
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = max(dp[i - 1][0] + dishes[i][1], dp[i - 1][1])
    # print(dp)

print(max(dp[-1]))
