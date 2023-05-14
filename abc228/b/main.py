n,x=map(int,input().split())
a=[0]+list(map(int,input().split()))

lis=[False]*(n+1)
tmp=x
lis[x]=True
while True:
    tmp=a[tmp]
    if lis[tmp]:
        break
    else:
        lis[tmp]=True
print(lis.count(True))
