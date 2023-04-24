s = input()

bl = s.find("B")
br = s.rfind("B")

if bl % 2 == br % 2:
    print("No")
    exit()

rl = s.find("R")
rr = s.rfind("R")
k = s.find("K")

if rl < k < rr:
    print("Yes")
else:
    print("No")
