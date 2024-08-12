n, a, x, y = map(int, input().split())
print(x * n - max(0, n - a) * (x - y))
