MOD = 998244353
n = int(input())

memo = [n % MOD]

for i in range(60):
    memo.append((memo[-1] * 10 ** len(str(memo[-1])) + memo[-1]) % MOD)

bi = []
for i in range(60, -1, -1):
    if n >= 2**i:
        n -= 2**i
        bi.append(i)

bi.reverse()

ans = memo[bi.pop()]
for x in bi:
    ans = (ans * 10 ** len(str(memo[x])) + memo[x]) % MOD

print(ans)
