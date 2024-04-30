n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n):
    for j in range(i + 1, n):
        b.append(a[i] * a[j])


print(len(b & a) * 2)
