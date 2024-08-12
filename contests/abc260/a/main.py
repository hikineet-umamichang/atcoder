s = list(input())
if len(set(s)) == 1:
    print(-1)
    exit()

s.sort()
if s[0] == s[1]:
    print(s[2])
elif s[1] == s[2]:
    print(s[0])
else:
    print(s[0])
