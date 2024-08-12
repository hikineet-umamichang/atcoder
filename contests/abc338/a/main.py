s = list(input())
s1 = s[0]
s2 = "".join(s[1:])

if s1 == s1.upper() and s2 == s2.lower():
    print("Yes")
else:
    print("No")
