n, m = map(int, input().split())
s = [input() for _ in range(n)]

ans = 15
for bit in range(1, 2**n):
    tmp = [False] * m
    tmp2 = []
    for i in range(n):
        if bit & (1 << i):
            tmp2.append(i)
            for j in range(m):
                tmp[j] = tmp[j] or s[i][j] == "o"
    # print(bin(bit))
    # print(tmp2)
    # print(tmp)
    if sum(tmp) == m:
        ans = min(ans, bit.bit_count())

print(ans)
