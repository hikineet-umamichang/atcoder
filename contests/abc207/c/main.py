n = int(input())
L, R = [], []
for _ in range(n):
    t, l, r = map(int, input().split())
    if t == 1:
        l = l * 2
        r = r * 2 + 1
    elif t == 2:
        l = l * 2
        r = r * 2
    elif t == 3:
        l = l * 2 + 1
        r = r * 2 + 1
    else:
        l = l * 2 + 1
        r = r * 2
    L.append(l)
    R.append(r)

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        a = max(L[i], L[j])
        b = min(R[i], R[j])
        if a < b:
            ans += 1

print(ans)
