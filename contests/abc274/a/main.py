b, a = map(int, input().split())
ans = a * 100000 // b
if b == a:
    print("1.000")
elif a == 0:
    print("0.000")
else:
    print("0." + str(round(ans / 100)))
