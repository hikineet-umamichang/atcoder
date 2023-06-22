t = int(input())


def solve():
    n = int(input())
    if n == 1:
        print("B")
        return

    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    s = input()
    color = ["#"] * n

    for i in range(n):
        if len(G[i]) == 1 and color[G[i][0]] == "#":
            color[G[i][0]] = s[G[i][0]]
        elif len(G[i]) == 1 and color[G[i][0]] != "#":
            if color[G[i][0]] != s[G[i][0]]:
                print(-1)
                return
    ans = "".join(color)
    ans = ans.replace("#", "B")
    print(ans)
    return


for _ in range(t):
    solve()
