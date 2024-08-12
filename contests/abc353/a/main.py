n = int(input())
h = list(map(int, input().split()))

for i in range(1, n):
    if h[i] > h[0]:
        print(i + 1)
        exit()
print(-1)
