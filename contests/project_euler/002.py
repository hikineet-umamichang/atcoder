n = int(input())

a = [1]
tmp = 2
ans = 0
i = 1
while tmp <= n:
    a.append(tmp)
    if tmp % 2 == 0:
        ans += tmp

    tmp = a[i - 1] + a[i]
    i += 1
print(ans)
print(a)
