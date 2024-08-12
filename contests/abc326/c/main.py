n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
r = 0
for l in range(n):
    while r < n and a[r] < a[l] + m:
        r += 1

    ans = max(ans, r - l)

print(ans)
