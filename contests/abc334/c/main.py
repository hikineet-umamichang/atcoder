from itertools import accumulate

n, k = map(int, input().split())
a = list(map(int, input().split()))

if (n - k) % 2 == 0:
    ans = 0
    for i in range(1, k, 2):
        ans += abs(a[i] - a[i - 1])
    print(ans)
else:
    front, back = [0], [0]
    for i in range(1, k - 1, 2):
        front.append(abs(a[i] - a[i - 1]))
        back.append(abs(a[-i] - a[-i - 1]))
    front = list(accumulate(front))
    back = list(accumulate(back))

    back.reverse()

    ans = 10**18
    for i in range(len(front) - 1):
        ans = min(ans, front[i] + back[i + 1])
    print(ans)
    print(front)
    print(back)
