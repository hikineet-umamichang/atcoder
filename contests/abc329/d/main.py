n, m = map(int, input().split())
a = list(map(int, input().split()))

b = [0] * (n + 1)
ans = 0
for i in range(m):
    b[a[i]] += 1
    if b[a[i]] > b[ans] or (b[a[i]] == b[ans] and a[i] < ans):
        print(a[i])
        ans = a[i]
    else:
        print(ans)
