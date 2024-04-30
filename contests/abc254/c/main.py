n, k = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a)

c = [[] for _ in range(k)]
for i in range(n):
    c[i % k].append(a[i])

for x in c:
    x.sort()

d = []
for i in range(n):
    d.append(c[i % k][i // k])

if b == d:
    print("Yes")
else:
    print("No")
