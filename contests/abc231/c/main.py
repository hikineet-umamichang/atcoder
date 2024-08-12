from bisect import bisect_left

n, q = map(int, input().split())
a = list(map(int, input().split()))
query = [int(input()) for _ in range(q)]

a.sort()

for q in query:
    print(n - bisect_left(a, q))
