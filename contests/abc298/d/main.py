import collections

q = int(input())
md = 998244353

s = 1
ln = 1
sd = collections.deque()
sd.append(1)

for _ in range(q):
    a = list(map(int, input().split()))

    if a[0] == 1:
        sd.append(a[1])
        s = ((s * 10) % md + a[1]) % md
        ln += 1
    elif a[0] == 2:
        ln -= 1
        tmp = sd.popleft()
        s = (s - (tmp * pow(10,ln,md))) % md
    else:
        print(s)
    # print(s,sd)
