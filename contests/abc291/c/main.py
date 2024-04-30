n=int(input())
s=input()

ans={(0,0)}
tempx=0
tempy=0
for x in s:
    if x=="R":
        tempx+=1
    elif x=="L":
        tempx-=1
    elif x=="U":
        tempy+=1
    else:
        tempy-=1
    if (tempx,tempy) in ans:
        print("Yes")
        exit()
    else:
        ans.add((tempx,tempy))
print("No")