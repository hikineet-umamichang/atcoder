n = int(input())
a = list(map(int, input().split()))

ans = 0
while True:
    ans += 1
    a.sort(reverse=True)
    a[0] -= 1
    a[1] -= 1

    cnt = 0
    for x in a:
        if x > 0:
            cnt += 1
    if cnt <= 1:
        break
print(ans)
