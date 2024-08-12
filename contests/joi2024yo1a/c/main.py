n = int(input())
s, t = [input() for _ in range(2)]
ans = 0
for i in range(n):
    ans += int(s[i] != t[i])
print(ans)
