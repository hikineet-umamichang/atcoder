from itertools import accumulate

n = int(input())
s = list(map(int, input().replace("(", " 1").replace(")", " -1").split()))

if list(accumulate(s)).count(-1):
    print("No")
else:
    print("Yes")
