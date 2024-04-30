n, x = map(int, input().split())
a = list(map(int, input().split()))

aa = set(a)
aaa = set([x + tmp for tmp in a])

if len(aa & aaa):
    print("Yes")
else:
    print("No")
