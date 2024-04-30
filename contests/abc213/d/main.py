n = int(input())
cities = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())

    cities[a].append(b)
    cities[b].append(a)

for x in cities:
    x.sort()

memo = [False] * (n + 1)
ans = [1]


def dfs(city, memo):
    memo[city] = True

    for x in cities[city]:
        if not memo[x]:
            ans.append(x)
            dfs(x, memo)


print(*ans)
