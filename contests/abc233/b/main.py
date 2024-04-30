l, r = map(int, input().split())
s = list(input())

ans=s[:l-1]+s[l-1:r][::-1]+ s[r:]

ans="".join(ans)
print(ans)
