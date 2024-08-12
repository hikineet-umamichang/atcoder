from math import factorial

p = int(input())
coins = [factorial(i) for i in range(10, 0, -1)]

ans = 0
for x in coins:
    tmp = p // x
    ans += tmp
    p -= tmp * x

print(ans)
