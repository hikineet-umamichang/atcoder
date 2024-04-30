n = int(input())

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1 - i - j):
            if i * i + j * j - k * k == 0 and i + j + k == 1000:
                print(i * j * k)
                print(i, j, k)
                exit()
