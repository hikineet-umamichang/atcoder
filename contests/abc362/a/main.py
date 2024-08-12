R, G, B = map(int, input().split())
C = input()
if C == "Red":
    R += 1000
elif C == "Green":
    G += 1000
else:
    B += 1000
print(min(R, G, B))
