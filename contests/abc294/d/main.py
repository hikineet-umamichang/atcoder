n,q=map(int,input().split())

ls=[True]*n
mn=0
mx=0
for _ in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        mn+=1
    elif a[0]==3:
        for i in range(mx,mn):
            if ls[i]==True:
                print(i+1)
                break
            else:
                mx+=1
    else:
        ls[a[1]-1]=False
