n = int(input()) - 1

cnt_3 = n // 3
cnt_5 = n // 5
cnt_15 = n // 15

ans = (
    (cnt_3 + 1) * cnt_3 // 2 * 3
    + (cnt_5 + 1) * cnt_5 // 2 * 5
    - (cnt_15 + 1) * cnt_15 // 2 * 15
)

print(ans)
