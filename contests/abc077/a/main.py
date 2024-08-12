c1, c2 = [list(input()) for _ in range(2)]
c2 = list(reversed(c2))
print("YES" if c1 == c2 else "NO")
