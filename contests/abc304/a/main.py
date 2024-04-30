n = int(input())
s = []
a = []
for _ in range(n):
    ss, aa = input().split()
    s.append(ss)
    a.append(int(aa))

min_idx = a.index(min(a))

for i in range(n):
    print(s[(min_idx + i) % n])
