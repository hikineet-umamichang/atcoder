n, k = map(int, input().split())

if k < (n - 1) * 2 or k % 2 == 1:
    print("No")
else:
    print("Yes")
