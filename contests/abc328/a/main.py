n, x = map(int, input().split())
print(sum([i if i <= x else 0 for i in list(map(int, input().split()))]))
