n, a = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
for x in t:
    if ans > x:
        ans = (ans - x) + x + a
    else:
        ans = x + a

    print(ans)
