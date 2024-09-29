s = [input() for _ in range(12)]

ans = 0
for idx, x in enumerate(s):
    if idx + 1 == len(x):
        ans += 1
print(ans)
