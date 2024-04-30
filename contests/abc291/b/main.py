n=int(input())
x=sorted(list(map(int,input().split())))

ans=x[n:4*n]
#print(ans)
print(sum(ans)/len(ans))
