n, x = map(int, input().split())
a = []
for _ in range(n):
    l, *b = map(int, input().split())
    a.append(b)

tmp=[a[0]]
for i in range(1,n):
    
