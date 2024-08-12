h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
c = list(zip(*c))

ans = []
for x in c:
    tmp = "".join(x).count("#")
    ans.append(tmp)
print(*ans)
