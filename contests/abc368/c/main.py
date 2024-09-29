n = int(input())
h = list(map(int, input().split()))

ans = 0

for x in h:
    while ans % 3 and x > 0:
        if ans % 3 == 1:
            x -= 1
            ans += 1
        elif ans % 3 == 2:
            x -= 3
            ans += 1
    if x <= 0:
        continue

    d, m = divmod(x, 5)
    ans += d * 3
    if m == 0:
        continue
    elif m == 1:
        ans += 1
    elif m == 2:
        ans += 2
    else:
        ans += 3
print(ans)
