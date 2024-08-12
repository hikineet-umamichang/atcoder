s = input()
a = s[:3]
b = int(s[3:])

if a == "ABC" and 0 < b < 350 and b != 316:
    print("Yes")
else:
    print("No")
