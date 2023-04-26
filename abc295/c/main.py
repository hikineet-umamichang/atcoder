n = int(input())
a = sorted(list(map(int, input().split())))

cnt = 0
i = 0
while i < n - 1:
    if a[i] == a[i + 1]:
        cnt += 1
        i += 2
    else:
        i += 1

print(cnt)
