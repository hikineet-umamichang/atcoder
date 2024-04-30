n = int(input())


def calc_divisors(N):
    # 答えを表す集合
    res = []

    # 各整数 i が N の約数かどうかを調べる
    for i in range(1, N + 1):
        # √N で打ち切り
        if i * i > N:
            break

        # i が N の約数でない場合はスキップ
        if N % i != 0:
            continue

        # i は約数である
        res.append(i)

        # N ÷ i も約数である (重複に注意)
        if N // i != i:
            res.append(N // i)

    # 約数を小さい順に並び替えて出力
    res.sort()
    return res


triangle_num = [1]
now_len = 1
while True:
    now_len += 1
    triangle_num.append(triangle_num[-1] + now_len)
    if len(calc_divisors(triangle_num[-1])) > n:
        print(triangle_num[-1])
        print(calc_divisors(triangle_num[-1]))
        exit()
