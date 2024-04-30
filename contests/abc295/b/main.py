r, c = map(int, input().split())
b = [list(input()) for _ in range(r)]


def bomb(x, y, impact):
    for i in range(r):
        for j in range(c):
            if b[i][j] == "#" and abs(i - x) + abs(j - y) <= impact:
                b[i][j] = "."


for i in range(r):
    for j in range(c):
        if b[i][j].isnumeric():
            bomb(i, j, int(b[i][j]))
            b[i][j]="."

for x in b:
    print(*x,sep="")
