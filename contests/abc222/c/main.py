n, m = map(int, input().split())
a = [input() for _ in range(n * 2)]

b = [i for i in range(2 * n)]


def battle(x, y):
    if x == y:
        return 0
    elif x == "G" and y == "C":
        return 1
    elif x == "C" and y == "P":
        return 1
    elif x == "P" and y == "G":
        return 1
    else:
        return -1


for i in range(m):
    for k in range(n):
        pleyer1 = (a[b[2 * k] % 1000][i], b[2 * k] % 1000 + 1)
        pleyer2 = (a[b[2 * k + 1] % 1000][i], b[2 * k + 1] % 1000 + 1)

        result = battle(pleyer1[0], pleyer2[0])

        if result == 1:
            b[2 * k] -= 1000
        elif result == -1:
            b[2 * k + 1] -= 1000
        # print(pleyer1, pleyer2, result)
    b.sort()
    # print(b)

for x in b:
    print(x % 1000 + 1)
