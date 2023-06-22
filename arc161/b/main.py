t = int(input())


def solve(num):
    if num < 7:
        return -1

    while bin(num).count("1") < 3:
        num -= 1

    tmp = bin(num)[2:]
    ans = ""
    cnt = 0
    for i in range(len(tmp)):
        if tmp[i] == "1" and cnt < 3:
            ans += "1"
            cnt += 1
        else:
            ans += "0"
    return int(ans, 2)


for _ in range(t):
    n = int(input())
    print(solve(n))
