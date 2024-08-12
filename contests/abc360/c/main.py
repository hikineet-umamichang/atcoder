n = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

boxes = [[] for _ in range(n)]
for idx, x in enumerate(a):
    boxes[x - 1].append(w[idx])

ans = 0
for x in boxes:
    if x == []:
        continue
    x.sort()
    ans += sum(x) - x[-1]

print(ans)
