n = int(input())
a = list(map(int, input().split()))

a.sort()
c = []
prv = 0
cnt = 0
for x in a:
    if prv == x:
        cnt += 1
    else:
        prv = x
        c.append(cnt)
        cnt = 1
c.append(cnt)

ans = n * (n - 1) // 2
for x in c:
    ans -= x * (x - 1) // 2
print(ans)
