n, m = map(int, input().split())

if m == 0:
    print(*[i for i in range(1, n + 1)])
    exit()

a = list(map(int, input().split()))

ans = []
l = 1
while l <= n:
    r = l
    while r in a:
        r += 1
    for i in range(r, l - 1, -1):
        ans.append(i)
    l = r + 1
print(*ans)
