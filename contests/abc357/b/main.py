s = input()

u, l = 0, 0
for i in range(len(s)):
    if s[i].lower() == s[i]:
        l += 1
    else:
        u += 1

if u > l:
    print(s.upper())
else:
    print(s.lower())
