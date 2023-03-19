n = int(input())
a = []
for _ in range(n):
    a.append(input())

for i in range(n):
    for j in range(i, n):
        tempa = a[i][j]
        tempb = a[j][i]

        if i == j:
            if tempa != "-":
                print("incorrect")
                exit()

        if tempa == "D":
            if tempb != "D":
                print("incorrect")
                exit()

        if tempa == "W":
            if tempb != "L":
                print("incorrect")
                exit()

        if tempa == "L":
            if tempb != "W":
                print("incorrect")
                exit()

print("correct")
