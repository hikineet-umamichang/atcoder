n=int(input())
q=int(input())

box=[[] for _ in range(n+1)]
cards=[set() for _ in range(2*10**5+1)]
for _ in range(q):
    a=list(map(int,input().split()))

    if a[0]==1:
        box[a[2]].append(a[1])
        cards[a[1]].add(a[2])
    elif a[0]==2:
        print(*sorted(box[a[1]]))
    else:
        print(*sorted(list(cards[a[1]])))
