n = int(input())
s = input()
t = input()

ans = True

for i in range(n):
    # print(s[i], t[i])
    if s[i] == "1" and t[i] == "l":
        continue
    elif s[i] == "l" and t[i] == "1":
        continue
    elif s[i] == "o" and t[i] == "0":
        continue
    elif s[i] == "0" and t[i] == "o":
        continue
    elif s[i] != t[i]:
        ans = False
if ans:
    print("Yes")
else:
    print("No")
