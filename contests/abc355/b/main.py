n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):
    a[i] += 0.1

c = a + b
c.sort()
# print(*c)
for i in range(n + m - 1):
    if c[i] - int(c[i]) > 0 and c[i + 1] - int(c[i + 1]) > 0:
        print("Yes")
        exit()
print("No")
