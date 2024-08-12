n = int(input())
a = list(map(int, input().split()))
print(*(set(range(min(a), max(a) + 1)) - set(a)))
