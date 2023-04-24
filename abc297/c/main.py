h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w - 1):
        if s[i][j] == "T" and s[i][j + 1] == "T":
            s[i][j] = "P"
            s[i][j + 1] = "C"

for x in s:
    print("".join(x))
