n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

for i in range(q):
    if max(a) == a[l[i] - 1]:
        continue

    if a[l[i] - 1] + 1 in a and a[l[i] - 1] + 1 <= n:
        a[l[i] - 1] += 1
    else:
        continue

print(*a)
