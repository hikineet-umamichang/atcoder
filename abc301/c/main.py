s = input()
t = input()

x = "@abcdefghijklmnopqrstuvwxyz"
s_cnt = [s.count(x[i]) for i in range(27)]
t_cnt = [t.count(x[i]) for i in range(27)]

# print(s_cnt)
# print(t_cnt)
s_at = s_cnt[0]
t_at = t_cnt[0]

for i in range(1, 27):
    if s_cnt[i] != t_cnt[i] and not (x[i] in "atcoder"):
        print("No")
        exit()
    elif s_cnt[i] > t_cnt[i]:
        t_at -= abs(s_cnt[i] - t_cnt[i])
    elif s_cnt[i] < t_cnt[i]:
        s_at -= abs(t_cnt[i] - s_cnt[i])


if s_at >= 0 and t_at >= 0:
    print("Yes")
else:
    print("No")
