h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]

# print(*a, sep="\n")
# print(*b, sep="\n")

for i in range(h):
    for j in range(w):
        flg = True
        for y in range(h):
            for x in range(w):
                if b[y][x] != a[(y + i) % h][(x + j) % w]:
                    flg = False
        if flg:
            print("Yes")
            exit()
print("No")
