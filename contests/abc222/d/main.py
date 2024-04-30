n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab_diff = [b[i] - a[i] for i in range(n)]

dp = [[0] * (b[-1] - a[0]) for _ in range(n)]

print(*dp, sep="\n")
print(ab_diff)
