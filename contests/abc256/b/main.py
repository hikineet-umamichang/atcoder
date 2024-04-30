from collections import deque

n = int(input())
a = list(map(int, input().split()))

base = deque([0] * 4)
p = 0
for i in range(n):
    base[0] = 1
    for j in range(a[i]):
        p += base.pop()
    while len(base) < 4:
        base.appendleft(0)

print(p)
