import operator

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []
for i in range(n):
    c.append([a[i], 0, i, 0])
for i in range(m):
    c.append([b[i], 1, i, 0])

c.sort()

for i in range(n + m):
    c[i][3] = i+1

aa, bb = [], []

for x in c:
    if x[1] == 0:
        aa.append(x)
    else:
        bb.append(x)

aa.sort(key=operator.itemgetter(2))
bb.sort(key=operator.itemgetter(2))

for x in aa:
    print(x[3], end=" ")
print("\n",end="")
for x in bb:
    print(x[3], end=" ")
print("\n",end="")
