L,n1,n2=map(int,input().split())
a=[]
for _ in range(n1):
    v,l=map(int,input().split())
    a.extend([v]*l)

b=[]
for _ in range(n2):
    v,l=map(int,input().split())
    b.extend([v]*l)

ans=0
for i in range(L):
    if a[i]==b[i]:
        ans+=1
# print(a)
# print(b)

print(ans)