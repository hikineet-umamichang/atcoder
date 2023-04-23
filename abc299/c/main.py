n = int(input())
s = input()

if not ("-" in s and "o" in s):
    print(-1)
    exit()

mx = 0
for i in range(n):
    if s[i] != "-":
        continue

    cnt = 1
    while i + cnt < n:
        if s[i + cnt] == "o":
            cnt += 1
        else:
            break

    mx = max(mx, cnt - 1)

for i in range(n-1,-1,-1):
    if s[i] != "-":
        continue

    cnt = 1
    while i - cnt >=0:
        if s[i - cnt] == "o":
            cnt += 1
        else:
            break

    mx = max(mx, cnt - 1)


print(mx)
