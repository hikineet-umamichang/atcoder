s = input()
ss = list(s)
ss.sort()

if ss[0] == ss[1]:
    print(s.index(ss[-1]) + 1)
else:
    print(s.index(ss[0]) + 1)
