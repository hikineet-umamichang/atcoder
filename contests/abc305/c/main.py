# h, w = map(int, input().split())
# s = [input() for _ in range(h)]

# x_ls = []
# y_ls = []

# for i in range(h):
#     for j in range(w):
#         if s[i][j] == "#":
#             x_ls.append(j)
#             y_ls.append(i)

# y_ls.sort()
# x_ls.sort()

# y1 = min(y_ls)
# y2 = max(y_ls)
# x1 = min(x_ls)
# x2 = max(x_ls)

# for i in range(y1, y2 + 1):
#     for j in range(x1, x2 + 1):
#         if s[i][j] != "#":
#             print(i + 1, j + 1)


h, w = map(int, input().split())
s = [["."] + list(input()) + ["."] for _ in range(h)]
s = [["."] * (w + 2)] + s + [["."] * (w + 2)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == "#":
            continue

        if (s[i - 1][j] == "#" or s[i + 1][j] == "#") and (
            s[i][j - 1] == "#" or s[i][j + 1] == "#"
        ):
            print(*[i, j])
            exit()
