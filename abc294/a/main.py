n=int(input())
a=list(map(int,input().split()))

b=[]
for x in a:
    if x%2==0:
        b.append(x)

print(*b)