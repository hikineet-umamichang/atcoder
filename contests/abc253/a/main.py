abc = list(map(int, input().split()))
b = abc[1]
abc.sort()
if b == abc[1]:
    print("Yes")
else:
    print("No")
