s = input()
t = input()

ans = []
cnt = 0
for i in range(len(t)):
    if t[i] == s[cnt]:
        ans.append(i + 1)
        cnt += 1

print(*ans)
