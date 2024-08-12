n = int(input())
s = [input() for _ in range(n)]
mx = 0
for x in s:
    mx = max(mx, len(x))

ans = [[] for _ in range(mx)]
for i in range(n):
    for j in range(mx):
        if j >= len(s[i]):
            ans[j].append("*")
        else:
            ans[j].append(s[i][j])

for x in ans:
    print("".join(reversed(x)).rstrip("*"))
