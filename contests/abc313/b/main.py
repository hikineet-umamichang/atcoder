n, m = map(int, input().split())
rank = set(range(1, n + 1))

for _ in range(m):
    a, b = map(int, input().split())
    rank.discard(b)

if len(rank) != 1:
    print(-1)
else:
    print(rank.pop())
