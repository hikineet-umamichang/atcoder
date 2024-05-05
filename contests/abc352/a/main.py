n, x, y, z = map(int, input().split())

if x > y:
    x, y = y, x

if x < z < y:
    print("Yes")
else:
    print("No")
