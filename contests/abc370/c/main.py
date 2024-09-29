s = list(input())
t = list(input())

ans = []
while "".join(s) != "".join(t):
    tmp = []
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        prev = s[i]
        s[i] = t[i]
        tmp.append(("".join(s), i))
        s[i] = prev

    tmp.sort()
    s[tmp[0][1]] = t[tmp[0][1]]
    ans.append("".join(s))

print(len(ans))
print(*ans, sep="\n")
