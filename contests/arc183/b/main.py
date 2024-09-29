from collections import deque


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    seen = [True] * n
    for i in range(n):
        if a[i] != b[i]:
            seen[i] = False


T = int(input())

for _ in range(T):
    if solve():
        print("Yes")
    else:
        print("No")
