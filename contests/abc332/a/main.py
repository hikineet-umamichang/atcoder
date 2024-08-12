n, s, k = map(int, input().split())
ans = 0
for _ in range(n):
    p, q = map(int, input().split())
    ans += p * q
print(ans + (k if ans < s else 0))
