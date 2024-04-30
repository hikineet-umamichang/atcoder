n = int(input())
s = input()

import math

tak = 0
aok = 0

kati = math.ceil(n / 2)

for x in s:
    if x == "T":
        tak += 1
    else:
        aok += 1
    if tak >= kati:
        print("T")
        exit()
    elif aok >= kati:
        print("A")
        exit()
