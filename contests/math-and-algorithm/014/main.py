n = int(input())

ans = []

for i in range(2, int(n**0.5) + 1):
    while n > 1:
        if n % i:
            break

        ans.append(i)
        n //= i
if n != 1:
    ans.append(n)

print(*ans)
