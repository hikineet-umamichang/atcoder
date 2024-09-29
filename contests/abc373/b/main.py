s = input()
ans = 0
for i in range(25):
    ans += abs(s.index(chr(i + 65)) - s.index(chr(i + 66)))
print(ans)
