n, k = map(int, input().split())
s = input()
ans = ""
for i in range(n):
    if ans.count("o") < k and s[i] == "o":
        ans += "o"
    else:
        ans += "x"
print(ans)
