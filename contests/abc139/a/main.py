s, t = [list(input()) for _ in range(2)]
print(sum([1 if x == y else 0 for x, y in zip(s, t)]))
