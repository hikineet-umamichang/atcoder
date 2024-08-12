from bisect import bisect_left

n, h, x = map(int, input().split())
p = list(map(int, input().split()))
print(bisect_left(p, x - h) + 1)
