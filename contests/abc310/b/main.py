n, m = map(int, input().split())
goods = []
for _ in range(n):
    pcf = list(map(int, input().split()))
    p = pcf[0]
    f = set(pcf[2:])
    goods.append((p, f))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if not goods[i][0] <= goods[j][0]:
            continue
        if not goods[i][1] >= goods[j][1]:
            continue

        if goods[i][0] < goods[j][0] or goods[i][1] > goods[j][1]:
            print("Yes")
            exit()
print("No")
