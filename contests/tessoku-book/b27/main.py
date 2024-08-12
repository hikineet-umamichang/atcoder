a, b = map(int, input().split())
ab = [a, b]

while True:
    if a > b:
        a, b = b, a
    if a * b == 0:
        gcd = a + b
        break

    b = b % a

print(ab[0] * ab[1] // gcd)
