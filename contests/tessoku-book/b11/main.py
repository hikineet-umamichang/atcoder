n = int(input())
a = list(map(int, input().split()))
q = int(input())
x = [int(input()) for _ in range(q)]

a.sort()

for y in x:
    ok, ng = n, -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if a[mid] >= y:
            ok = mid
        else:
            ng = mid

    print(ok)
