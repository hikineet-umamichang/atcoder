n, m = map(int, input().split())
a = list(map(int, input().split()))
x = [list(map(int, input().split())) for _ in range(n)]
b = [0] * m

for i in range(n):
    for j in range(m):
        b[j] += x[i][j]


for aa, bb in zip(a, b):
    if aa > bb:
        print("No")
        exit()
print("Yes")
