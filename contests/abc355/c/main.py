n, t = map(int, input().split())
a = list(map(int, input().split()))

ans_row = [0] * n
ans_col = [0] * n
ans_dia1 = 0
ans_dia2 = 0

for i in range(t):
    tmp_row = (a[i] - 1) // n
    tmp_col = (a[i] - 1) % n
    ans_row[tmp_row] += 1
    ans_col[tmp_col] += 1

    if tmp_row == tmp_col:
        ans_dia1 += 1

    if tmp_row == n - tmp_col - 1:
        ans_dia2 += 1

    # print([ans_row[tmp_row], ans_col[tmp_col], ans_dia1, ans_dia2])

    if max([ans_row[tmp_row], ans_col[tmp_col], ans_dia1, ans_dia2]) == n:
        print(i + 1)
        exit()

print(-1)
