h, w = map(int, input().split())
si, sj = map(int, input().split())
c = (
    [["#"] * (w + 2)]
    + [["#"] + list(input()) + ["#"] for _ in range(h)]
    + [["#"] * (w + 2)]
)
x = list(input())

for a in x:
    if a == "U":
        dxy = (-1, 0)
    elif a == "D":
        dxy = (1, 0)
    elif a == "L":
        dxy = (0, -1)
    else:
        dxy = (0, 1)

    if c[si + dxy[0]][sj + dxy[1]] == ".":
        si += dxy[0]
        sj += dxy[1]

print(*[si, sj])
