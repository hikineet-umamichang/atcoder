n = int(input())
a = list(map(int, input().split()))
a.sort()
_ = a.pop(0)

cnt = 1
for i in range(1, n - 1):
    if a[i] == a[i - 1]:
        cnt += 1
    else:
        cnt = 1
    if cnt > n // 2:
        print("No")
        exit()
print("Yes")
