n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [
    [(0 if x == "x" else 1) * a[idx] for idx, x in enumerate(input())] for _ in range(n)
]

mx = max([sum(x) + idx + 1 for idx, x in enumerate(s)])

for i in range(n):
    rest = [x - s[i][idx] for idx, x in enumerate(a)]
    rest.sort(reverse=True)

    tmp = sum(s[i]) + i + 1
    for j in range(m):
        if tmp >= mx:
            print(j)
            break
        tmp += rest[j]
