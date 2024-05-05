n = int(input())
price = 1.08 * n // 1
if price < 206:
    print("Yay!")
elif price == 206:
    print("so-so")
else:
    print(":(")
