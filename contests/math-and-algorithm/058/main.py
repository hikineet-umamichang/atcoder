n, x, y = map(int, input().split())

dist = abs(x) + abs(y)
if dist > n or (dist - n) % 2:
    print("No")
else:
    print("Yes")
