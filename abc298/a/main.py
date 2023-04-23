n=int(input())
s=input()

for x in s:
    if x=="x":
        print("No")
        exit()

for x in s:
    if x=="o":
        print("Yes")
        exit()

print("No")
