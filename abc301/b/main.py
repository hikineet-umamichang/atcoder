n = int(input())
a = list(map(int, input().split()))
i = 0
while i < len(a) - 1:
    if a[i] - a[i + 1] < -1:
        x = list(range(a[i] + 1, a[i + 1]))
        a[i + 1 : i + 1] = x
    elif a[i] - a[i + 1] > 1:
        x = list(range(a[i] - 1, a[i + 1], -1))
        a[i+1:i+1] = x
    i += 1
print(*a)
