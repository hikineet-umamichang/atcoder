n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

for i in range(q):
    #print(a[l[i] - 1] + 1)
    if not a[l[i] - 1] + 1 in a and a[l[i] - 1]+1 <= n:
        a[l[i] - 1] += 1
    else:
        continue
    #print(*a)

print(*a)
