MOD = 10**9 + 7

n = int(input())
a = list(input())

tmp = 1
b = []
for i in range(1, n):
    if a[i] == a[i - 1]:
        if tmp > 1:
            b.append((tmp + 1) // 2)
        tmp = 1
    else:
        tmp += 1

if tmp > 1:
    b.append((tmp + 1) // 2)


ans = 1
for x in b:
    ans = (ans * x) % MOD
print(ans)
