s = list(input())

for i in range(len(s)):
    if i % 2 == 1 and s[i] == "1":
        print("No")
        exit()
print("Yes")
