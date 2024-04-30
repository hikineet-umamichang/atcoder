n=int(input())
a=list(map(int,input().split()))

b=[0]*(n+1)
for idx,x in enumerate(a):
    b[x]=idx+1
print(*b[1:])