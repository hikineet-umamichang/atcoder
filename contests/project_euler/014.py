def collatz_sequence(n):
    length = 1
    while True:
        if n == 1:
            break
        elif n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2
        length += 1
        # print(n)
    return length


n = int(input())
mx = 0
for i in range(1, n):
    tmp = collatz_sequence(i)
    if mx < tmp:
        ans = i
    mx = max(tmp, mx)
print(ans)

