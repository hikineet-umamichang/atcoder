from itertools import permutations


def solve(n, k):
    l = []
    for i in range(k):
        tmp = list(range(1, n + 1))
        l += tmp
    l.sort(reverse=True)

    if n == 1:
        print(*l)
        exit()
    # print(l)
    if n % 2 == 1:
        for _ in range(k):
            l.remove((n + 1) // 2)
        l.remove(n // 2)
        l = [(n + 1) // 2] * k + [n // 2] + l
        print(*l)
    else:
        l.remove(n // 2)
        l = [n // 2] + l
        print(*l)


def main():
    n, k = map(int, input().split())
    solve(n, k)


main()
