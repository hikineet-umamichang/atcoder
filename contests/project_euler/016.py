n = int(input())

s = list(str(2**n))

ans = 0
for x in s:
    ans += int(x)
print(ans)
