s = input()
ans = []
for i in range(len(s) // 2):
    ans.append(s[2 * i + 1])
    ans.append(s[2 * i])

print(*ans, sep="")
