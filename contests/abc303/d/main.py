x,y,z=map(int,input().split())
s=list(input())

dp=[[0, 0] for _ in range(len(s))]
if s[0]=='a':
    dp[0]=[x,z+y]
else:
    dp[0]=[y,z+x]

for i in range(1,len(s)):
    # print(i,dp)
    if s[i]=='a':
        dp[i][0]=min(dp[i-1][0]+x,dp[i-1][1]+z+x)
        dp[i][1]=min(dp[i-1][0]+z+y,dp[i-1][1]+y)
    else:
        dp[i][0]=min(dp[i-1][0]+y,dp[i-1][1]+z+y)
        dp[i][1]=min(dp[i-1][0]+z+x,dp[i-1][1]+x)
print(min(dp[-1]))