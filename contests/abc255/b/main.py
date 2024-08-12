from bisect import bisect_left

n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]

aa = set(a)


def is_ok(arg):
    tmp = [False] * n

    for i in range(k):
        for j in range(n):
            if tmp[j] or j + 1 in aa:
                continue

            nx, ny = xy[j][0], xy[j][1]
            kx, ky = xy[a[i] - 1][0], xy[a[i] - 1][1]

            if arg >= ((nx - kx) ** 2 + (ny - ky) ** 2) ** 0.5:
                tmp[j] = True

    return sum(tmp) == n - k


def meguru_bisect(ng, ok):
    while abs(ok - ng) > pow(10, -5):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, 10**10))
