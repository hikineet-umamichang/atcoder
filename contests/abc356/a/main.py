n, l, r = map(int, input().split())
a = list(range(1, n + 1))
print(*(a[: l - 1] + a[l - 1 : r][::-1] + a[r:]))
