from bisect import bisect

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = [0] * m
for idx, x in enumerate(b):
    i = bisect(a, x)

    if i >= 1:
        ans[idx] = max(k - abs(a[i - 1] - x), 0, ans[idx])
    if i < n:
        ans[idx] = max(k - abs(a[i] - x), 0, ans[idx])


print(*ans, sep="\n")
