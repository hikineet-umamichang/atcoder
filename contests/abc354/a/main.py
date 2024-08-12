h = int(input())
tmp = 0
i = 0
while True:
    tmp += 2**i
    i += 1
    if tmp > h:
        print(i)
        exit()
