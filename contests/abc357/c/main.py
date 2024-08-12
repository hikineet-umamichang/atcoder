import numpy as np

n = int(input())


def solve(num):
    if num == 0:
        return np.array([["#"]])

    prev = solve(num - 1)
    center = np.array([["."] * 3 ** (num - 1) for _ in range(3 ** (num - 1))])

    tmp0 = np.concatenate((prev, prev, prev), axis=1)
    tmp1 = np.concatenate((prev, center, prev), axis=1)

    return np.concatenate((tmp0, tmp1, tmp0), axis=0)


for x in solve(n):
    print(*x, sep="")
