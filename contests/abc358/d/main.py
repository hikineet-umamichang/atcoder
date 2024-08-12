from sortedcontainers import SortedList

n, m = map(int, input().split())
a = SortedList(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for x in b:
    i = a.bisect_left(x)
    if i == len(a):
        exit(print(-1))

    ans += a[i]
    a.pop(i)
print(ans)
