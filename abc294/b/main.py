h,w=map(int,input().split())
a=[]
for _ in range(h):
    a.append(list(map(int,input().split())))

b=[]
for i in range(h):
    b.append([])
    for j in range(w):
        if a[i][j]==0:
            b[i].append(".")
        else:
            b[i].append(chr(64+a[i][j]))

for x in b:
    print(*x,sep="")