import math

a, b = map(int, input().split())

if a > b:
    a, b = b, a

ans = 0
while a > 0:
    ans += b // a
    b = b % a
    a, b = b, a

print(ans - 1)
