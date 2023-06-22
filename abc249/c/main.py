n, k = map(int, input().split())
s = [list(set(list(input()))) for _ in range(n)]

ans = 0

# print(s)
for i in range(2**n):
    table = [0] * 26
    for j in range(n):
        # print(bin(i),j,i ^ 1 << j)
        if i & 1 << j:
            for x in s[j]:
                table[ord(x) - 97] += 1

    # print(table)
    tmp = 0
    for x in table:
        if x == k:
            tmp += 1
    ans = max(ans, tmp)
print(ans)
