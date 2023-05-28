h, w = map(int, input().split())

s = [list(map(int, input().split())) for _ in range(h)]
for _ in range(4):
    s.append([0] * w)
for x in s:
    x.extend([0, 0, 0, 0])
print(*s, sep="\n")

ans = 0
for y in range(h):
    for x in range(w):
        tmp_row = 1
        tmp_column = 1
        tmp_diagonal1 = 1
        tmp_diagonal2 = 1
        for i in range(4):
            tmp_row *= s[y][x + i]
            tmp_column *= s[y + i][x]
            tmp_diagonal1 *= s[y + i][x + i]
            if x >= 3:
                tmp_diagonal2 *= s[y + i][x - i]
        ans = max(ans, tmp_row, tmp_column, tmp_diagonal1, tmp_diagonal2)

print(ans)
