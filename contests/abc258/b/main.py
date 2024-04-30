n = int(input())
a = []
for _ in range(n):
    a.append(list(input()))
# print(a)


def solve(x, y):
    dx = [-1, 1, 0, 1, -1, 0, -1, 1]
    dy = [-1, 1, 1, 0, 1, -1, 0, -1]

    mx = 0
    for ddx, ddy in zip(dx, dy):
        temp = 0
        for i in range(n):
            temp = temp * 10 + int(a[(x + ddx * i) % n][(y + ddy * i) % n])
        mx = max(temp, mx)

    return mx


ans = -1
for i in range(n):
    for j in range(n):
        ans = max(ans, solve(i, j))

print(ans)
