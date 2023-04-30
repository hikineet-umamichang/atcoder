h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = [0] * min(h, w)
checked = []


def is_cross(y, x):
    d = 1
    for d in range(1, min(y, x, h - y, w - x) + 1):
        if not (
            c[y + d][x + d] == "#"
            and c[y + d][x - d] == "#"
            and c[y - d][x + d] == "#"
            and c[y - d][x - d] == "#"
        ):
            return

    d += 1

    flg = False
    try:
        if c[y + d][x + d] == ".":
            flg = True
    except IndexError:
        pass

    try:
        if c[y + d][x - d] == ".":
            flg = True
    except IndexError:
        pass

    try:
        if c[y - d][x + d] == ".":
            flg = True
    except IndexError:
        pass

    try:
        if c[y - d][x - d] == ".":
            flg = True
    except IndexError:
        pass

    if flg:
        ans[d - 2] += 1
        print(y, x, d)

    return


for i in range(1, h - 1):
    for j in range(1, w - 1):
        if c[i][j] == "#":
            is_cross(i, j)

print(*ans)
