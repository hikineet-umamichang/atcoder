from math import lcm

n = int(input())
a = list(map(int, input().split()))

print(lcm(*a))
