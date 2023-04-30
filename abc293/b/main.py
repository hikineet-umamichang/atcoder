n = int(input())
a = list(map(int, input().split()))

all = set([i for i in range(1, n + 1)])
called = set()

for i in range(n):
    if not i + 1 in called:
        called.add(a[i])

ans = all - called
ans = sorted(list(ans))

print(len(ans))
print(*ans)
