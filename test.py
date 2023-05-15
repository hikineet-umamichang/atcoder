n, k = map(int, input().split())
a = list(map(int, input().split()))

b = []

for l in range(n - 1):
    for r in range(l + 1, n):
        b.append(a[:l] + a[r:l:-1] + a[r:])
b.sort()

print(*b[k - 1])
