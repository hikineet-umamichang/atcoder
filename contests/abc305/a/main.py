n = int(input())
ans = 0
for i in range(0, 101, 5):
    if abs(n - i) < abs(n - ans):
        ans = i
print(ans)
