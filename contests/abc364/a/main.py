n = int(input())
s = [input() for _ in range(n)]

s.pop()
s = "".join(s)
if "sweetsweet" in s:
    print("No")
else:
    print("Yes")
