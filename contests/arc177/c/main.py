n = int(input())
c = [input() for _ in range(n)]

cr = [list(map(int, x.replace("R", "0").replace("B", "1"))) for x in c]
cr = [[-float("INF") if y else float("INF") for y in x] for x in cr]
cb = [[-float("INF") if y > 0 else float("INF") for y in x] for x in cr]


cr[0][0] = 0
cb[n - 1][0] = 0

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(i, j, prev):
    global cr
    for i in range(n):
        for j in range(n):
            for dx, dy in dxy:
                tmp_i, tmp_j = i + dx, j + dy
                if tmp_i < 0 or n <= tmp_i or tmp_j < 0 or n <= tmp_j:
                    continue

                if prev <= 0 and cr[tmp_i][tmp_j] < 0 and prev > cr[tmp_i][tmp_j]:
                    cr[tmp_i][tmp_j] = prev - 1
                    dfs(tmp_i, tmp_j, prev - 1)
                elif (
                    prev <= 0 and cr[tmp_i][tmp_j] > 0 and prev >= cr[tmp_i][tmp_j] * -1
                ):
                    cr[tmp_i][tmp_j] = prev * -1 + 1
                    dfs(tmp_i, tmp_j, prev * -1 + 1)
                elif prev >= 0 and cr[tmp_i][tmp_j] > 0 and prev >= cr[tmp_i][tmp_j]:
                    cr[tmp_i][tmp_j] = prev
                    dfs(tmp_i, tmp_j, prev)


def dfs2(i, j, prev):
    global cb
    for i in range(n):
        for j in range(n):
            for dx, dy in dxy:
                tmp_i, tmp_j = i + dx, j + dy
                if tmp_i < 0 or n <= tmp_i or tmp_j < 0 or n <= tmp_j:
                    continue

                if prev <= 0 and cb[tmp_i][tmp_j] < 0 and prev > cb[tmp_i][tmp_j]:
                    cb[tmp_i][tmp_j] = prev - 1
                    dfs2(tmp_i, tmp_j, prev - 1)
                elif (
                    prev <= 0 and cb[tmp_i][tmp_j] > 0 and prev >= cb[tmp_i][tmp_j] * -1
                ):
                    cb[tmp_i][tmp_j] = prev * -1 + 1
                    dfs2(tmp_i, tmp_j, prev * -1 + 1)
                elif prev >= 0 and cb[tmp_i][tmp_j] > 0 and prev >= cb[tmp_i][tmp_j]:
                    cb[tmp_i][tmp_j] = prev
                    dfs2(tmp_i, tmp_j, prev)


dfs(0, -1, 0)
dfs2(n - 1, -1, 0)

print(cr[-1][-1])
print(cb[0][n - 1])

print(*cr, sep="\n")
print(*cb, sep="\n")
