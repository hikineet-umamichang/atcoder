k = int(input())
c = list(map(int, input().split()))
MOD = 998244353


def solve(num):
    pass


ans = 0
for i in range(1, k + 1):
    ans = (ans + solve(i)) % MOD

print(ans)
