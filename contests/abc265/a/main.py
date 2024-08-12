x, y, n = map(int, input().split())

if y / 3 < x:
    print(n // 3 * y + n % 3 * x)
else:
    print(n * x)
