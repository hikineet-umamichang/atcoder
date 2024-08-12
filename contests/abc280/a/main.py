h, w = map(int, input().split())
s = [input().count("#") for _ in range(h)]
print(sum(s))
