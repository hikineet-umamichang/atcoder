n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

try:
    for x in b:
        a.remove(x)
except ValueError:
    print("No")
    exit()

print("Yes")