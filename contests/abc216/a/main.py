x, y = map(int, input().split("."))
if y < 3:
    z = "-"
elif y < 7:
    z = ""
else:
    z = "+"
print(str(x) + z)
