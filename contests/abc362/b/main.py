xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

ab = abs(xa - xb) ** 2 + abs(ya - yb) ** 2
bc = abs(xc - xb) ** 2 + abs(yc - yb) ** 2
ac = abs(xa - xc) ** 2 + abs(ya - yc) ** 2

if sum([ab, bc, ac]) == max(ab, bc, ac) * 2:
    print("Yes")
else:
    print("No")
