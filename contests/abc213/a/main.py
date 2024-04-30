a, b = map(int, input().split())

for i in range(0,256):
    if a ^ i == b:
        print(i)
        exit()
    