h, w = map(int, input().split())
s = [input() for _ in range(h)]

x_ls = []
y_ls = []

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            x_ls.append(j)
            y_ls.append(i)

y_ls.sort()
x_ls.sort()

y1 = min(y_ls)
y2 = max(y_ls)
x1 = min(x_ls)
x2 = max(x_ls)

for i in range(y1, y2 + 1):
    for j in range(x1, x2 + 1):
        if s[i][j] != "#":
            print(i + 1, j + 1)
