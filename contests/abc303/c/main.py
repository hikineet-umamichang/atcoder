n, m, h, k = map(int, input().split())
s = input()

xy = set()
for _ in range(m):
    x, y = map(int, input().split())
    xy.add(x * 10**6 + y)
seen = set()

tmp = 0
for x in s:
    if x == "R":
        tmp += 10**6
    elif x == "L":
        tmp -= 10**6
    elif x == "U":
        tmp += 1
    else:
        tmp -= 1
    h -= 1
    if h == -1:
        print("No")
        exit()

    if tmp in xy and not (tmp in seen):
        if h < k:
            h = k
            seen.add(tmp)
print("Yes")
