t = int(input())


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if a[i] <= i + 1 and min(a[i+1:]+[10**5]) >= a[i]:
            cnt += 1
    print(cnt)


for _ in range(t):
    solve()
