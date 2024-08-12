n, x = map(int, input().split())
a = list(map(int, input().split()))

mx, mn = max(a), min(a)
mid = sum(a) - mx - mn
if x - mid <= mn:
    print(0)
elif x - mid > mx:
    print(-1)
else:
    print(x - mid)
