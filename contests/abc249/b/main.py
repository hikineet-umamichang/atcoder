s = input()

up = False
dn = False

for x in s:
    if x.isupper():
        up = True
    else:
        dn = True

if len(set(list(s))) == len(s) and up and dn:
    print("Yes")
else:
    print("No")
