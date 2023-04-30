n, q = map(int, input().split())

players = [0]*(n+1)
for _ in range(q):
    a, x = map(int, input().split())

    if a==1:
        players[x]+=1
    elif a==2:
        players[x]+=2
    else:
        if players[x]>=2:
            print('Yes')
        else:
            print('No')
