n, k = map(int, input().split())
a = list(map(int, input().split()))
aa = filter(lambda x: x % k == 0, a)
print(*[x // k for x in aa])
