from math import gcd

n = int(input())
a = list(map(int, input().split()))

print(gcd(*a))
