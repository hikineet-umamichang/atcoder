a, b = map(int, input().split())
length = (a**2 + b**2) ** 0.5
print(*[a / length, b / length])
