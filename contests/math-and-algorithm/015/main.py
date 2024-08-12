a, b = map(int, input().split())
while True:
    if a > b:
        a, b = b, a

    if a * b == 0:
        gcd = a + b
        break

    b %= a

print(gcd)
