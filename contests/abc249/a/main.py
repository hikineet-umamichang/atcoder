a, b, c, d, e, f, x = map(int, input().split())

tak, aok = 0, 0

tak += x // (a + c) * a * b + min(x % (a + c), a) * b
aok = x // (d + f) * d * e + min(x % (d + f), d) * e

if tak > aok:
    print("Takahashi")
elif tak < aok:
    print("Aoki")
else:
    print("Draw")
