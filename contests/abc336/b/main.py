n = int(input())
i = 0
while True:
    if n % (2**i) != 0:
        print(i - 1)
        exit()
    i += 1
