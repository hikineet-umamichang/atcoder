import math
a,b=map(int,input().split())

cnt=0
while a>=1 and b>=1:
    g=math.gcd(a,b)

    a-=g
    b-=g
    cnt+=1
print(cnt)