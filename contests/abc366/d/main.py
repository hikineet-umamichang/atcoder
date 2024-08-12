n = int(input())
cuboid = []

for i in range(n):
    cuboid.append([])
    for j in range(n):
        cuboid[i].append(list(map(int, input().split())))

cubsum = []
for a in cuboid:
    tmp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tmp[i][j] = tmp[i][j - 1] + a[i - 1][j - 1]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tmp[i][j] = tmp[i - 1][j] + tmp[i][j]
    cubsum.append(tmp)


# for x in cubsum:
#     print(*x, sep="\n")
#     print()

q = int(input())
for _ in range(q):
    lx, rx, ly, ry, lz, rz = map(int, input().split())

    ans = 0
    # print([lx - 1, rx])
    for i in range(lx - 1, rx):
        ans += cubsum[i][ry][rz]
        ans += cubsum[i][ly - 1][lz - 1]
        ans -= cubsum[i][ly - 1][rz]
        ans -= cubsum[i][ry][lz - 1]

    print(ans)
