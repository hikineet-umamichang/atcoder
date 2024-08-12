a = list(map(int, list(input())))
tmp = 10
for x in a:
    if tmp <= x:
        print("No")
        exit()
    tmp = x
print("Yes")
