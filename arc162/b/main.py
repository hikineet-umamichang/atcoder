n = int(input())
p = list(map(int, input().split()))
import copy

q = copy.deepcopy(p)
y = 0
while len(q) != n % 2:
    flg = True
    i = 0
    while i < len(q) - 1:
        if q[i] - q[i + 1] == -1:
            del q[i : i + 2]
            flg = False
        i += 1
    if len(q) == 1:
        y = q[0]
    if flg:
        print("No")
        exit()


import bisect

if y != 0:
    lf = [y]
else:
    lf = []
ans = []
r = copy.deepcopy(p)
while len(r) != n % 2:
    flg = True
    i = 0
    while i < len(r) - 1:
        if r[i] - r[i + 1] == -1:
            b = bisect.bisect_left(lf, r[i])
            lf = lf[:b] + r[i : i + 2] + lf[b:]
            del r[i : i + 2]
            flg = False

            if n % 2 == 1:
                ans.append([])
        i += 1
    if flg:
        break
