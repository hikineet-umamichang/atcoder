n, p = map(int, input().split())
print(len(list(filter(lambda x: x < p, list(map(int, input().split()))))))
