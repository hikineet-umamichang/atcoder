h, w = map(int, input().split())
G = [[0] + list(input()) + [0] for _ in range(h)]

G = [["0"] * (w + 2)] + G + [["0"] * (w + 2)]
x, y = 1, 1
route = []


while True:
    s = G[x][y]
    G[x][y] = "1"
    route.append([x, y])

    if s == "U":
        x -= 1
    elif s == "D":
        x += 1
    elif s == "L":
        y -= 1
    elif s == "R":
        y += 1
    elif s == "0":
        print(*route[-2])
        exit()
    elif s == "1":
        print(-1)
        exit()
