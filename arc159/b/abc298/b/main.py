n=int(input())

a,b=[],[]

for _ in range(n):
    a.append(list(map(int,input().split())))

for _ in range(n):
    b.append(list(map(int,input().split())))


tmp=a
prev=a
for _ in range(4):
    prev=tmp
    tmp=[]
    for x in zip(*prev[::-1]):
        tmp.append(list(x))
    
    flg=True
    for i in range(n):
        for j in range(n):
            if tmp[i][j]==1:
                if b[i][j]!=1:
                    flg=False
    # print(prev)
    # print(tmp)
    # print(b,"\n")

    if flg:
        print("Yes")
        exit()

print("No")

