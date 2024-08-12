n, s = [input() for _ in range(2)]
if "ABC" in s:
    print(s.index("ABC") + 1)
else:
    print(-1)
