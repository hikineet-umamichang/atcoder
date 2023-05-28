n = int(input()) + 1

G = [[1] * n for _ in range(n)]

for i in range(1, n):
    for j in range(1, n):
        G[i][j] = G[i - 1][j] + G[i][j - 1]

print(G[-1][-1])
