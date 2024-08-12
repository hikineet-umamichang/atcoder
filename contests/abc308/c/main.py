n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

c = [[x[0] * 10**30 // (x[0] + x[1]) + n - idx, idx] for idx, x in enumerate(ab)]
c.sort(reverse=True)

for x in c:
    print(x[1] + 1, end=" ")
