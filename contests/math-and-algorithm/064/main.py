n, k = map(int, input().split())
a = sum(map(int, input().split()))

if a > k or (k - a) % 2:
    print("No")
else:
    print("Yes")
