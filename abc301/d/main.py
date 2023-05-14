s = list(input())
n = int(input())

s.reverse()

tmp = 0
ls = []
for i in range(len(s)):
    if s[i] == "1":
        tmp += 1 << i
    elif s[i] == "?":
        ls.append(1 << i)
if tmp > n:
    print(-1)
    exit()

# print("tmp", tmp)
# print("ls", ls)

for x in reversed(ls):
    if n - tmp >= x:
        tmp += x

# print("tmp", tmp)


print(tmp)
