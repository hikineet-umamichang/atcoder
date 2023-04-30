h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

ans = 0
seen = []


def dfs(x, y, seen):
    global ans
    seen.append(a[x][y])

    if x == h - 1 and y == w - 1:
        if len(set(seen)) == h + w - 1:
            ans += 1
        return

    if x < h - 1:
        dfs(x + 1, y, seen)
    if y < w - 1:
        dfs(x, y + 1, seen)


dfs(0, 0, seen)

print(ans)
